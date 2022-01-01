from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

names = {"ken": {"age": 19, "gender": "male"},
        "bill": {"age":70, "gender": "male"}}

class HelloWorld(Resource):
    def get(self, name):
        return names[name]


api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == '__main__':
    app.run(debug=True)