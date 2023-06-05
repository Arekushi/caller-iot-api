from src.namespaces.student import student_ns
from flask_restx import fields, Model


student_model = Model('student', {
    'ra': fields.Integer,
    'full_name': fields.String
})
student_ns.add_model('student', student_model)
