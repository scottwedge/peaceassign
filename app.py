import os
from db import db
from resources.user import User
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
    data = []
    with open('data.json') as f:
        
        json_data = json.loads(f.read())
        for i in range(len(json_data)):
            data.append(json_data[i])
            

    fields = [
        "id",
        "first_name",
        "last_name",
        "company_name",
        "city",
        "state",
        "zip",
        "email",
        "web" ,
        "age"
    ]

    for item in data:
        my_data = [item[field] for field in fields]
        insert_query = "INSERT INTO users VALUES (%d, %s, %s, %s, %s, %s, %d, %s, %d)"
        db.engine.execute(insert_query, tuple(my_data))

api.add_resource(User, '/api/users/<int:user_id>')



db.init_app(app)
if __name__ == '__main__':
    app.run(port=5000, debug=True)