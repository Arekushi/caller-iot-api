from src.exceptions import UnauthenticatedException
from src.api import api

from prisma.errors import PrismaError, MissingRequiredValueError


@api.errorhandler(UnauthenticatedException)
def unauthenticated_handler(error):
    return {
        'message': error.message
    }, 403


@api.errorhandler(MissingRequiredValueError)
def required_value_handler(error):
    return {
        'message': error
    }, 400


@api.errorhandler(PrismaError)
def prisma_error_handler(error):
    return {
        'message': error
    }, 500
