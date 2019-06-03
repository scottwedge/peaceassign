from flask_restful import Resource, reqparse
from models.user import UserModel
import json

_user_parser = reqparse.RequestParser()

class UserRegister(Resource):
    
    def get(self):
        users = UserModel.query.fetchall()
        def result_dict(r):
            return dict(zip(r.keys(), r))

        return list(map(result_dict, users))

    
    def post(self, data):
        data = _user_parser.parse_args()

        if UserModel.find_by_id(data['id']):
            return {"message": "A user with that id already exists"}, 400

        user = UserModel(data['id'], data['first_name'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201



class User(Resource):

    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404
        return user.json(), 200

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted.'}, 200

