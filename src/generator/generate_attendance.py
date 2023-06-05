import random
from datetime import datetime, timedelta
from src.services.student_service import get_all_students
from src.services.attendance_service import create_many_attendances


async def insert_attendances():
    students = await get_all_students()
    list_to_insert = list()
    
    for i, student in enumerate(students):
        ra = student.ra
        list_to_insert.append({
            'ra': ra,
            'attendances': list()
        })
        
        for _ in range(0, random.randint(1, 30)):
            day = random.randint(1, 30)
            hour = random.randint(19, 22)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            
            date = datetime(2023, 4, day, hour, minute, second)
            
            list_to_insert[i]['attendances'].append({
                "created_at": date.strftime("%Y-%m-%d %H:%M:%S")
            })
    
    await create_many_attendances(list_to_insert)
