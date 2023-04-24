import os
import importlib
from datetime import timedelta

# must be updated to inlude addtional secrets/ api keys & use a gitignored custom-config file instad
def load_config():
    config = {'ENV': os.environ.get('ENV', 'DEVELOPMENT')}
    delta = 7
    if config['ENV'] == "DEVELOPMENT":
        from .default_config import JWT_ACCESS_TOKEN_EXPIRES, SQLALCHEMY_DATABASE_URI, SECRET_KEY
        config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
        config['SECRET_KEY'] = SECRET_KEY
        delta = JWT_ACCESS_TOKEN_EXPIRES
    else:
        config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
        config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        config['DEBUG'] = config['ENV'].upper() != 'PRODUCTION'
        delta = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 7))

        # Define PayPal credentials
        config['PAYPAL_CLIENT_ID'] = os.environ.get('PAYPAL_CLIENT_ID')
        config['PAYPAL_CLIENT_SECRET'] = os.environ.get('PAYPAL_CLIENT_SECRET')

    config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=int(delta))
    config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    config['TEMPLATES_AUTO_RELOAD'] = True
    config['SEVER_NAME'] = '0.0.0.0'
    config['PREFERRED_URL_SCHEME'] = 'https'
    config['UPLOADED_PHOTOS_DEST'] = "App/uploads"
    config["JWT_TOKEN_LOCATION"] = ["headers"]
    config['PAYPAL_CLIENT_ID'] = 'Afvt_KPFyp5JNthwGwxwVQ5yhbx9xavzNE5M9I1ScoZx7Z2STSPzyaDLtgQYvxAhzsWbhkuS_SDEGhhc'
    config['PAYPAL_CLIENT_SECRET'] = 'EPYFY_2gOAIXO6OZc9KYgAMc-epWClcl2jD3rbzuZQCnB4uWSYv60HUH4C6zF8yGIcuRvyqVZpjwvPzv'
    return config

config = load_config()