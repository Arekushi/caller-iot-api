from src.namespaces.attendance import attendance_ns
from flask_restx import fields, Model


attendance_model = Model('attendance', {
    'created_at': fields.DateTime(dt_format='iso8601')
})


student_model = Model('student', {
    'ra': fields.Integer(required=True),
    'attendances': fields.List(fields.Nested(attendance_model), required=True)
})

attendance_ns.add_model('student', student_model)
attendance_ns.add_model('attendance', attendance_model)
