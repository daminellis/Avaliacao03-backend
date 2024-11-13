from service.user_service import get_all_users
from service.user_service import get_user_by_id
from service.user_service import create_user
from service.user_service import update_user
from service.user_service import delete_user

from flask import request
from flask_jwt_extended import jwt_required

#Repository
from repository.user.create_user_repository import UserRepository
from repository.user.update_user_repository import UpdateUserRepository

def users(app):
    @app.route('/users', methods=['GET'])
    @jwt_required()
    def get_all_users_route():
        return get_all_users()

    @app.route('/users/<int:id>', methods=['GET'])
    @jwt_required()
    def get_user_by_id_route(id):
        return get_user_by_id(id)

    @app.route('/user', methods=['POST'])
    def create_user_route():
        data = request.get_json()
        user_rep = UserRepository(data['first_name'], data['last_name'], data['age'], data['password'])
        return create_user(user_rep)

    @app.route('/users/<int:id>', methods=['PATCH'])
    @jwt_required()
    def update_user_route(id):
        data = request.get_json()
        update_user_rep = UpdateUserRepository(data['first_name'], data['last_name'], data['age'], data['password'])
        return update_user(id, update_user_rep)

    @app.route('/users/<int:id>', methods=['DELETE'])
    @jwt_required()
    def delete_user_route(id):
        return delete_user(id)