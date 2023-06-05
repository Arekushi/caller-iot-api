from src.namespaces.attendance import attendance_ns
from src.exceptions import StudentNotFoundException


@attendance_ns.errorhandler(StudentNotFoundException)
def handle_student_not_found(error):   
    return {
        'message': error.message
    }, 404
