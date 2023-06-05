from flask_httpauth import HTTPTokenAuth

token_auth = HTTPTokenAuth(scheme='Bearer')
