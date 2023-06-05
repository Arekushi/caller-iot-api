from src.services.student_service import create_student

students = [
    'ALEXANDRE LIMA',
    'ARIANE CRISTINA',
    'CAIO PECELLIN COSTA',
    'LUCIANA ROMUALDO',
    'LUCIANA ROMUALDO',
    'VINICIUS MARTINS',
    'ISABELLE RIBEIRO',
    'MARINA GAMA',
    'LUCAS DEL PUERTO'
]

async def insert_students():
    for student in students:
        await create_student({
            'full_name': student
        })
