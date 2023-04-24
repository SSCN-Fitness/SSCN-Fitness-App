import os
import paypalrestsdk
from flask import Flask, jsonify, request

# Set up the PayPal API client
paypalrestsdk.configure({
  "mode": "sandbox", # Use "live" for production
  "client_id": os.environ.get('PAYPAL_CLIENT_ID'),
  "client_secret": os.environ.get('PAYPAL_CLIENT_SECRET')
})

app = Flask(__name__)

@app.route('/pay', methods=['POST'])
def process_payment():
    # Get the payment information from the request
    payment_amount = request.json['amount']
    payment_currency = request.json['currency']
    payment_description = request.json['description']
    payment_return_url = request.json['return_url']
    payment_cancel_url = request.json['cancel_url']
    
    # Set up the payment object
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": payment_return_url,
            "cancel_url": payment_cancel_url
        },
        "transactions": [{
            "amount": {
                "total": payment_amount,
                "currency": payment_currency
            },
            "description": payment_description
        }]
    })

    # Create the payment
    if payment.create():
        # Redirect the user to PayPal to complete the payment
        for link in payment.links:
            if link.method == "REDIRECT":
                redirect_url = link.href
                return jsonify({'redirect_url': redirect_url})
    else:
        # Handle payment creation failure
        return jsonify({'error': payment.error})