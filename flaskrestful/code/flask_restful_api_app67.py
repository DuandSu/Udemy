from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self, name):
        return {'student': name}

# http://127.0.0.1:5000/student/Rolf
api.add_resource(Student, '/student/<string:name>')

# port 5000 is default so argument not really necessary.
app.run(port=5000)