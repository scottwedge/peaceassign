from flask_restful import Resource, reqparse
from models.user import UserModel
from models.schema import UserSchema
from flask import jsonify, request

_user_parser = reqparse.RequestParser()
user_schema = UserSchema()
users_schema = UserSchema(many=True)

class UserRegister(Resource):
    
    def get(self):
        users = UserModel.query.all()
        result = users_schema.dump(users)
        return jsonify(result.data), 200

    def post(self):
        data = request.get_json()

        if UserModel.find_by_id(data['id']):
            return {"message": "A user with that id already exists"}, 400

        user = UserModel(data['id'], data['first_name'], data['last_name'], data['company_name'], data['city'], data['state'], data['zip'], data['website'], data['email'], data['age'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201



class User(Resource):

    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404
        result = user_schema.dump(user)
        return jsonify(result.data), 200

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted.'}, 200

