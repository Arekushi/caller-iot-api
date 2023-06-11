from prisma import Prisma
from datetime import datetime

from src.utils import datetime_from_str, time_ms_diff


async def create_subject(subject):
    prisma = Prisma()
    await prisma.connect()
    
    await prisma.subject.query_raw(
        """
        INSERT INTO
            subject(name, day_of_week, day_of_week_label, start_hour, end_hour, total_classes)
        VALUES
            ($1, $2, $3, CAST($4 as TIME), CAST($5 as TIME), $6)
        """,
        subject['name'],
        subject['day_of_week'],
        subject['day_of_week_label'],
        subject['start_hour'],
        subject['end_hour'],
        subject['total_classes']
    )
    
    await prisma.disconnect()


async def get_all_subjects():
    prisma = Prisma()
    await prisma.connect()
    
    subjects = await prisma.subject.find_many()
    
    await prisma.disconnect()
    return subjects


async def get_subject_by_datetime(created_at):
    prisma = Prisma()
    await prisma.connect()
    
    subject = await prisma.query_first(
        """
        SELECT
            *
        FROM
            subject
        WHERE
            CAST(start_hour as TIME) <= CAST($1 as TIME)
            AND CAST(end_hour as TIME) >= CAST($1 as TIME)
            AND day_of_week = $2
        """,
        created_at.time().strftime('%H:%M:%S'),
        created_at.weekday()
    )
    
    await prisma.disconnect()
    return subject


async def get_next_subject():
    prisma = Prisma()
    await prisma.connect()
    
    subject = await prisma.query_first(
        """
        SELECT
            *
        FROM
            subject
        WHERE
            CAST($1 as TIME) <= CAST(end_hour as TIME)
        ORDER BY
            day_of_week, end_hour
        """,
        datetime.now().strftime('%H:%M:%S')
    )
    print(subject)
    
    await prisma.disconnect()
    return subject


async def get_today_attendances(id):
    prisma = Prisma()
    await prisma.connect()
    
    attendances = await prisma.attendance.find_many(
        where={
            'AND': {
                'subject_id': {
                    'equals': id
                },
                'created_at': {
                    'gte': datetime.combine(datetime.now(), datetime.min.time()),
                    'lt': datetime.combine(datetime.now(), datetime.max.time())
                }
            }
        }
    )
    
    await prisma.disconnect()
    return attendances


async def time_ms_to_next_subject():
    next_subject = await get_next_subject()
    now = datetime.now()
    next_subject_start_hour = datetime_from_str(next_subject['start_hour'], '%H:%M:%S')
    time_ms = time_ms_diff(next_subject_start_hour, now)
    
    response = {
        'time_ms_next_subject': time_ms
    }
    
    if time_ms <= 0:
        next_subject_end_hour = datetime_from_str(next_subject['end_hour'], '%H:%M:%S')
        response['time_ms_end_class'] = time_ms_diff(next_subject_end_hour, now)
        
    return response
