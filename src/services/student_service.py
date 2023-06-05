from prisma import Prisma
from datetime import datetime

from prisma.errors import PrismaError


async def create_student(student_request):
    prisma = Prisma()
    await prisma.connect()
    
    student = await prisma.student.create({
        'full_name': student_request['full_name'],
        'ra': generate_ra()
    })
    
    await prisma.disconnect() 
    return student
    

async def get_all_students():
    prisma = Prisma()
    await prisma.connect()
    
    students = await prisma.student.find_many()
    
    await prisma.disconnect()
    return students


def generate_ra():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    ra = hour * 10000 + minute * 100 + second
    ra = str(ra).zfill(5)

    return int(ra)


async def get_student_by_ra(student_request):
    prisma = Prisma()
    await prisma.connect()
    
    student = await prisma.student.find_first(
        where={
            'ra': {
                'equals': student_request['ra']
            }
        }
    )
    
    await prisma.disconnect()
    return student
