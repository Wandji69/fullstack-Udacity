from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://collins:postgres.01@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)


db.create_all()


def __repr__(self):
    return f'<Person ID: {self.id}, name: {self.name}>'


@app.route('/')
def index():
    person = Person.query.all()
    return "Hello, " + person.name


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
