from flask import Flask, jsonify, request

app = Flask(__name__)

message = "Hello \"John\" in the <PLACE>world</PLACE>!\n"


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        some_json = request.get_json()
        return jsonify({"you sent": some_json}), 201
    else:
        return jsonify({"about": message})


@app.route("/multi/<int:num>", methods=['GET'])
def multiply(num):
    return jsonify({"result": num * 10})
    
    

if __name__ == '__main__':

    app.run(debug=True)


"""

https://www.youtube.com/watch?v=s_ht4AKnWZg

curl -v -H "Content-Type: application/json" -X POST -d '{"name": "John", "age": 10}' http://127.0.0.1:5000/

"""
