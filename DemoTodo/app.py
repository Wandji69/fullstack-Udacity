from crypt import methods
from operator import truediv
from os import abort
import sys
from flask import Flask, redirect, render_template, request, session, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://collins:postgres.01@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)


def __repr__(self):
    return f'<Todo {self.id} {self.description}>'


@app.route('/todos/create', methods=['POST'])
def create_todo():
    body = {}
    error = False
    try:
        description = request.get_json()['description']
        todo = Todo(description=description)
        body['description'] = todo.description
        db.session.add(todo)
        db.session.commit()
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
        if error == True:
            abort(400)
        else:
            return jsonify(body)


@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())


# always include this at the bottom of your code (port 3000 is only necessary in workspaces)
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=3000)
