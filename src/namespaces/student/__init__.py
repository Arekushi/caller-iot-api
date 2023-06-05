from flask_restx import Namespace


student_ns = Namespace(
    name='student',
    description='Operações referentes aos Alunos'
)

from .student_routes import *
from .student_models import *
