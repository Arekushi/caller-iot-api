from flask_restx import Namespace


subject_ns = Namespace(
    name='subject',
    description='Operações referentes as Disciplinas'
)

from .subject_models import *
from .subject_routes import *
