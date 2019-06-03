import os
from db import db
from ma import ma
from resources.user import User, UserRegister
import json
from flask import Flask
from flask_restful import Api

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = '12122huehbdhwqbdhb'
api = Api(app)

@app.route('/')
def hello_world():
	return 'Hello world'


@app.before_first_request
def create_tables():
    db.create_all()
    db.engine.execute('ALTER TABLE users RENAME COLUMN e_mail TO email')

api.add_resource(User, '/api/users/<int:user_id>')
api.add_resource(UserRegister, '/api/users')

db.init_app(app)

if __name__ == '__main__':
    
    app.run(port=5000, debug=True)