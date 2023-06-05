from flask_restx import Resource

from src.namespaces.student import student_ns
from src.namespaces.student.student_models import student_model

from src.utils import run_async
from src.auth import token_auth
from src.services import create_student, get_all_students


@student_ns.route('/create')
class CreateStudent(Resource):
    
    @token_auth.login_required
    @student_ns.expect(student_model, validate=True)
    def post(self):
        data = student_ns.payload
        result = run_async(create_student, data)
        
        return {
            'message': f'O estudante [{result.full_name}] foi criado com sucesso!'
        }


@student_ns.route('/get-all')
class GetAllStudents(Resource):
    
    @student_ns.marshal_with(student_model)
    @token_auth.login_required
    def get(self):
        return run_async(get_all_students)
