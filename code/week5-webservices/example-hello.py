from flask import Flask, url_for

app = Flask(__name__)

# http://127.0.0.1:5000/howdy
@app.route("/howdy")
def howdy():
    return "Howdy\n"

# http://127.0.0.1:5000/ahoy/
# http://127.0.0.1:5000/ahoy  (via redirect)
@app.route("/ahoy/")
def ahoy():
    return "Ahoy\n"

# http://127.0.0.1:5000/ahoy/sue/
# http://127.0.0.1:5000/ahoy/sue  (via redirect)
@app.route("/ahoy_name/<string:name>/")
def ahoy_name(name):
    return "Ahoy %s\n" % name


if __name__ == "__main__":
    with app.test_request_context():
        print(url_for('howdy'))
        print(url_for('ahoy'))
        print(url_for('ahoy_name', name="sue"))
    app.run(debug=True)

"""

The following works:
$ curl http://127.0.0.1:5000/ahoy_name/Sue/

But if you remove the trailing slash you need to tell curl to follow the
redirect, which it will not do automatically.
$ curl -L http://127.0.0.1:5000/ahoy_name/Sue

"""
