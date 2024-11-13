from service.user_service import get_all_users
from service.user_service import get_user_by_id
from service.user_service import create_user
from service.user_service import update_user
from service.user_service import delete_user

from flask import request
from flask_jwt_extended import jwt_required

#DTOS
from dtos.user.create_user_dto import UserDTO
from dtos.user.update_user_dto import UpdateUserDTO

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
        user_dto = UserDTO(data['first_name'], data['last_name'], data['age'], data['password'])
        return create_user(user_dto)

    @app.route('/users/<int:id>', methods=['PUT'])
    @jwt_required()
    def update_user_route(id):
        data = request.get_json()
        update_user_dto = UpdateUserDTO(data['first_name'], data['last_name'], data['age'], data['password'])
        return update_user(id, update_user_dto)

    @app.route('/users/<int:id>', methods=['DELETE'])
    @jwt_required()
    def delete_user_route(id):
        return delete_user(id)