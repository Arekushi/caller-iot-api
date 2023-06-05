from flask_restx import Resource

from src.namespaces.attendance import attendance_ns
from src.namespaces.attendance.attendance_models import student_model
from src.services import create_many_attendances
from src.auth import token_auth
from src.utils import run_async


@attendance_ns.route('/register')
class RegisterAttendances(Resource):
    
    @token_auth.login_required
    @attendance_ns.expect([student_model], validate=True)
    def post(self):
        data = attendance_ns.payload
        run_async(create_many_attendances, data)
