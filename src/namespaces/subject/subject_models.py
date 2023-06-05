from src.namespaces.subject import subject_ns
from flask_restx import fields, Model
from src.fields import TimeField

subject_model = Model('subject', {
    'id': fields.Integer,
    'name': fields.String(required=True),
    'day_of_week': fields.Integer(required=True),
    'day_of_week_label': fields.String(required=True),
    'start_hour': TimeField(required=True),
    'end_hour': TimeField(required=True),
    'total_classes': fields.Integer(required=True)
})
subject_ns.add_model('subject', subject_model)

attendance_model = Model('attendance', {
    'created_at': fields.DateTime(dt_format='iso8601')
})
subject_ns.add_model('attendance', attendance_model)

next_subject_model = Model('next_subject', {
    'time_ms_next_subject': fields.Integer(required=True),
    'time_ms_end_class': fields.Integer()
})
subject_ns.add_model('next_subject', next_subject_model)
