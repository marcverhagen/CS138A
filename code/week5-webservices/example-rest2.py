from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

message = "Hello <person>John</person>.\n"

class HelloWorld(Resource):
    def get(self):
        return {"about": message}
    def post(self):
        some_json = request.get_json()
        return {"you sent": some_json}, 201

class Multi(Resource):
    def get(self):
        return jsonify({"result": num * 10})

api.add_resource(HelloWorld, "/")
api.add_resource(Multi, "/multi/<int:num>")

if __name__ == '__main__':
    app.run(debug=True)


"""

https://www.youtube.com/watch?v=s_ht4AKnWZg

$ curl http://127.0.0.1:5000

$ curl -v -H "Content-Type: application/json" -X POST -d '{"name": "John", "age": 10}' http://127.0.0.1:5000/

"""
