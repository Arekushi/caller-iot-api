import os
from flask import Flask
from dynaconf import FlaskDynaconf

from src.api import config_api
from src.auth import token_auth

from src.exceptions import UnauthenticatedException


app = Flask(__name__)
FlaskDynaconf(app)


def create_app() -> Flask:
    api = config_api(app)
    api.init_app(app)
    
    return app


@token_auth.verify_token
def verify_token(token):
    tokens = [os.getenv('AUTH_TOKENS')]
    
    if token in tokens:
        return token

    raise UnauthenticatedException()
