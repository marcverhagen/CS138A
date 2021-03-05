from flask import Flask
from werkzeug.routing import Rule

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

# Using the following instead gives you more flexibility. The endpoint value in
# the rule and the argument of @app.endoint have to be the same. But you can
# change the name of the decorated function and if you want to change what URL
# you want to expose you can change the first argument to Rule().

# In Flask, an endpoint is an identifier that is used in determining what
# logical unit of your code should handle the request.

app.url_map.add(Rule('/howdy/', endpoint='howdy'))

@app.endpoint('howdy')
def howdy():
    return "Howdy"


if __name__ == "__main__":
    app.run(debug=True)
