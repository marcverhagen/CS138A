from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        name = request.args.get('name')
        return {"hello": name}
    def post(self):
        some_json = request.get_json()
        return {"hello": some_json['name']}, 201

class Multi(Resource):
    def get(self, num):
        return jsonify({"result": num * 10})
    
api.add_resource(Hello, "/hello")
api.add_resource(Multi, "/multi/<int:num>")


if __name__ == '__main__':
    app.run(debug=True)


"""

https://www.youtube.com/watch?v=s_ht4AKnWZg

$ curl http://127.0.0.1:5000/hello                # prints { "hello": null }

$ curl http://127.0.0.1:5000/hello?name=sue       # prints { "hello": "sue }

$ curl -H "Content-Type: application/json" -X POST -d '{"name": "John"}' http://127.0.0.1:5000/hello

$ curl http://127.0.0.1:5000/multi/10             # prints { "result": 100 }

$ curl http://127.0.0.1:5000/multi/ten            # 404 URL not found error

"""
