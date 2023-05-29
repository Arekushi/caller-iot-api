from flask import Flask
from flask_restx import Resource, Api
from dynaconf import FlaskDynaconf

app = Flask(__name__)
FlaskDynaconf(app)

api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {
            'hello': 'world'
        }


if __name__ == '__main__':
    app.run()
