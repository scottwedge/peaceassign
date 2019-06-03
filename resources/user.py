from flask_restful import Resource, reqparse
from models.user import UserModel
from flask import jsonify
from schema import UserSchema

_user_parser = reqparse.RequestParser()
users_schema = UserSchema()
class UserRegister(Resource):
    
    def get(self):
        users = UserModel.query.all()
        result = users_schema.dump(users)
        return jsonify(result.data)

    
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

