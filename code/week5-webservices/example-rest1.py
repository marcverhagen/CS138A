from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/hello", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify({"message": "Hello"})
    elif request.method == 'POST':
        some_json = request.get_json()
        return jsonify({"message": some_json['message']}), 201

@app.route("/multi/<int:num>", methods=['GET'])
def multiply(num):
    return jsonify({"result": num * 10})
    

if __name__ == '__main__':
    app.run(debug=True)


"""

https://www.youtube.com/watch?v=s_ht4AKnWZg

$ curl http://127.0.0.1:5000/hello                # prints { "message": "Hello" }

$ curl -v -H "Content-Type: application/json" -X POST -d '{"message": "Howdy"}' http://127.0.0.1:5000/hello

$ curl http://127.0.0.1:5000/multi/10             # prints { "result": 100 }

$ curl http://127.0.0.1:5000/multi/ten            # 404 URL not found error

"""
