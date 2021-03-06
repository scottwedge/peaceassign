from flask_restful import Resource
from models.user import UserModel
from models.schema import UserSchema
from flask import jsonify, request
from sqlalchemy import literal,or_

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class Users(Resource):

    @classmethod
    def get(self):
        users = UserModel.query
        args = request.args.to_dict()
        if args:
            if 'name' in request.args:
                users = users.filter(or_(UserModel.first_name.like('%' + request.args.get('name') + '%'), UserModel.last_name.like('%' + request.args.get('name') + '%')))
            if 'sort' in request.args:
                if '-' in request.args.get('sort'):
                    if 'age' in request.args.get('sort'):
                        users = users.order_by(UserModel.age.desc())
                    elif 'zip' in request.args.get('sort'):
                        users = users.order_by(UserModel.zip.desc())
                else:
                    if 'age' in request.args.get('sort'):
                        users = users.order_by(UserModel.age)
                    elif 'zip' in request.args.get('sort'):
                        users = users.order_by(UserModel.zip)
            if 'page' in request.args:
                if 'limit' in request.args:
                    users = users.paginate(int(request.args.get('page')), int(request.args.get('limit')), False)
                else:
                    users = users.paginate(int(request.args.get('page')), 5, False)
                users = users.items
        else: 
            users = users.all()
        result = users_schema.dump(users)
        return jsonify(result.data)

    @classmethod
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
        return jsonify(result.data)
    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted.'}

    @classmethod
    def put(cls, user_id: int):
        data = request.get_data()
        user = UserModel.find_by_id(user_id)
        for key, value in data.items():
            if args[key] is not None:
                setattr(user, key, value)
        return {}, 200


