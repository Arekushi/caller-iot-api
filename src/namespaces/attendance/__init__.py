from flask_restx import Namespace


attendance_ns = Namespace(
    name='attendance',
    description='Operações de registro de presença.'
)

from .attendance_models import *
from .attendance_routes import *
from .attendance_errorhandler import *
