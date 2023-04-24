from flask import Blueprint, request, jsonify
import paypalrestsdk

paypal_views = Blueprint('paypal', __name__)

paypalrestsdk.configure({
    "mode": "sandbox", # Change to "live" for production
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET"
})

@paypal_views.route('/payment', methods=['POST'])
def create_payment():
    # Get request data
    amount = request.json['amount']
    currency = request.json['currency']
    description = request.json['description']
    return_url = request.json['return_url']
    cancel_url = request.json['cancel_url']

    # Create payment object
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": return_url,
            "cancel_url": cancel_url
        },
        "transactions": [{
            "amount": {
                "total": amount,
                "currency": currency
            },
            "description": description
        }]
    })

    # Create payment
    if payment.create():
        # Return approval url for user to follow
        approval_url = [link.href for link in payment.links if link.rel == "approval_url"][0]
        return jsonify({'approval_url': approval_url}), 200
    else:
        # Return error message
        return jsonify({'message': payment.error}), 400