from prisma import Prisma

from src.services import get_subject_by_datetime, get_student_by_ra
from src.exceptions import StudentNotFoundException
from src.utils import datetime_from_str


async def create_many_attendances(students_request):
    prisma = Prisma()
    await prisma.connect()
    
    data = await generate_data(students_request)
    
    await prisma.attendance.create_many(data)
    await prisma.disconnect()


async def generate_data(students_request):
    attendances = []
     
    for student_request in students_request:
        student = await get_student_by_ra(student_request)
        
        if student:
            for attendance_request in student_request['attendances']:
                created_at = datetime_from_str(attendance_request['created_at'])
                subject = await get_subject_by_datetime(created_at)
                print('disciplina', subject)
                
                if subject:
                    attendances.append({
                        'created_at': created_at,
                        'subject_id': subject['id'],
                        'student_ra': student.ra
                    })
        else:
            raise StudentNotFoundException(student_request['ra'])
    
    return attendances
