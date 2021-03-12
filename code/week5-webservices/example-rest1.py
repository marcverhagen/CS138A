from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify({"message": "Hello"})
    elif request.method == 'POST':
        some_json = request.get_json()
        return jsonify({"message": some_json['message']}), 201

@app.route("/multi/<int:num1>,<int:num2>", methods=['GET'])
def multiply(num1, num2):
    return str({"result": num1 * num2})
    return jsonify({"result": num1 * num2})

if __name__ == '__main__':
    app.run(debug=True)

"""

$ curl -i http://127.0.0.1:5000/hello        # prints { "message": "Hello" }
$ curl -i http://127.0.0.1:5000/multi/10,10  # prints { "result": 100 }

$ curl \
    -i -H "Content-Type: application/json" -X POST -d '{"message": "Howdy"}' \
    http://127.0.0.1:5000/hello

"""
