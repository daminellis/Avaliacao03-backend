from controllers.user_controller import get_all_users
from controllers.user_controller import get_user_by_id
from controllers.user_controller import create_user
from controllers.user_controller import update_user
from controllers.user_controller import delete_user
from flask import request

#DTOS
from dtos.user.create_user_dto import UserDTO
from dtos.user.update_user_dto import UpdateUserDTO

def users(app):
    @app.route('/users', methods=['GET'])
    def get_all_users_route():
        return get_all_users()

    @app.route('/users/<int:id>', methods=['GET'])
    def get_user_by_id_route(id):
        return get_user_by_id(id)

    @app.route('/user', methods=['POST'])
    def create_user_route():
        data = request.get_json()
        user_dto = UserDTO(data['first_name'], data['last_name'], data['age'], data['password'])
        return create_user(user_dto)

    @app.route('/users/<int:id>', methods=['PUT'])
    def update_user_route(id):
        data = request.get_json()
        update_user_dto = UpdateUserDTO(data['first_name'], data['last_name'], data['age'], data['password'])
        return update_user(id, update_user_dto)

    @app.route('/users/<int:id>', methods=['DELETE'])
    def delete_user_route(id):
        return delete_user(id)