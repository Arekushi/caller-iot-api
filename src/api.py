from flask_restx import Api
from prisma import Prisma

from src.namespaces import student_ns, attendance_ns, subject_ns
from src.utils import run_async


api = Api(
    version='1.0',
    title='Caller IOT API',
    description='API para registro de chamada automática.',
    prefix='/api',
    authorizations={
        'Bearer Token': {
            'type': 'apiKey',
            'scheme': 'bearer',
            'name': 'Authorization',
            'in': 'header',
            'description': 'Enter the token with the `Bearer: ` prefix, e.g. "Bearer abcde12345".'
        }
    },
    security='Bearer Token'
)


namespaces = [
    attendance_ns,
    subject_ns,
    student_ns
]


def config_api(app) -> Api:
    config_namespaces()
    
    return api


def config_namespaces():
    for namespace in namespaces:
        api.add_namespace(namespace)


async def config_timezone():
    prisma = Prisma()
    await prisma.connect()
    await prisma.query_raw("SET timezone = '-03';")
    await prisma.disconnect()
