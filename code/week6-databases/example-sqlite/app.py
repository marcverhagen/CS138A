from flask import Flask
from flask import Flask, render_template
import db

app = Flask(__name__)
connection = db.DatabaseConnection('people.sqlite')

@app.route('/')
def all():
    rows = connection.get()
    return render_template('people.html', people=rows)

@app.route('/<string:name>')
def person(name):
    rows = connection.get(name)
    return f'{rows}\n'

@app.route('/<string:name>/<string:food>', methods=['POST'])
def add_person(name, food):
    connection.add(name, food)
    rows = connection.get(name)
    return f'{rows}\n'


if __name__ == '__main__':
    app.run(debug=True)


"""
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/jane
curl -X POST http://127.0.0.1:5000/john/bread
"""
