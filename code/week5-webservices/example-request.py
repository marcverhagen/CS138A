
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return ("%s\n" % request
            + "method=%s\n" % request.method
            + "arg=%s\n" % request.args.get('name')
            + "forms=%s\n" % request.form
            + "headers=\n%s\n" % request.headers)


if __name__ == "__main__":
    app.run(debug=True)

"""

https://werkzeug.palletsprojects.com/en/1.0.x/wrappers/

$ curl http://127.0.0.1:5000/?name=sue

$ curl -X POST -d"{}" http://127.0.0.1:5000/?name=sue

"""
