from flask import Flask, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://collins:postgres.01@localhost:5432/examples'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)


def __repr__(self):
    return f'<Todo {self.id} {self.description}>'


@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())


@app.route('/todo/create')
def create():
    description = request.form.get('description')
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

# always include this at the bottom of your code (port 3000 is only necessary in workspaces)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
