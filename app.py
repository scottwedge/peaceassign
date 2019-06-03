import os
from db import db
from resources.user import User, UserRegister
import json

from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow


app = Flask(__name__)
ma = Marshmallow(app)

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


api.add_resource(User, '/api/users/<int:user_id>')
api.add_resource(UserRegister, '/api/users')



db.init_app(app)

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "company_name", "city", "state", "zip", "website", "email", "age")


if __name__ == '__main__':
    
    app.run(port=5000, debug=True)