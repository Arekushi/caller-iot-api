from flask_restx import Resource

from src.namespaces.subject import subject_ns
from src.namespaces.subject.subject_models import subject_model, attendance_model, next_subject_model

from src.utils import run_async, datetime_from_str
from src.auth import token_auth
from src.services import create_subject, get_all_subjects, get_subject_by_datetime, \
    time_ms_to_next_subject, get_today_attendances


@subject_ns.route('/create')
class CreateSubject(Resource):
    
    @token_auth.login_required
    @subject_ns.expect(subject_model, validate=True)
    def post(self):
        data = subject_ns.payload
        run_async(create_subject, data)
        
        return {
            'message': f"A disciplina [{data['name']}] foi criada com sucesso!"
        }


@subject_ns.route('/get-all')
class GetAllSubjects(Resource):
    
    @subject_ns.marshal_with(subject_model)
    @token_auth.login_required
    def get(self):
        result = run_async(get_all_subjects)
        return result


@subject_ns.route('/get-by-time')
class GetByTime(Resource):
    
    @subject_ns.marshal_with(subject_model)
    @token_auth.login_required
    @subject_ns.expect(attendance_model, validate=True)
    def post(self):
        data = subject_ns.payload
        result = run_async(get_subject_by_datetime, datetime_from_str(data['created_at']))
        return result


@subject_ns.route('/next-subject')
class GetNextSubject(Resource):
    
    @subject_ns.marshal_with(next_subject_model)
    def get(self):
        result = run_async(time_ms_to_next_subject)
        return result
    

@subject_ns.route('/<int:id>/get-today-attendances')
class GetTodayAttendances(Resource):
    
    @subject_ns.marshal_with(attendance_model)
    def get(self, id):
        return run_async(get_today_attendances, id)
