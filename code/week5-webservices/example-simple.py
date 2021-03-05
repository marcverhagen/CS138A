from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello\n"

if __name__ == "__main__":
    app.run(debug=True)

"""

curl http://127.0.0.1:5000

"""
