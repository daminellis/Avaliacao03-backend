from controllers.user_controller import get_all_users
from controllers.user_controller import get_user_by_id
from controllers.user_controller import create_user
from controllers.user_controller import update_user
from controllers.user_controller import delete_user
from flask import request

#DTOS
from dtos.person.create_person_dto import PersonDTO
from dtos.person.update_person_dto import UpdatePersonDTO

def users(app):
    @app.route('/users', methods=['GET'])
    def get_all_persons_route():
        return get_all_users()

    @app.route('/users/<int:person_id>', methods=['GET'])
    def get_person_by_id_route(person_id):
        return get_user_by_id(person_id)

    @app.route('/user', methods=['POST'])
    def create_person_route():
        data = request.get_json()
        person_dto = PersonDTO(data['first_name'], data['last_name'], data['age'])
        return create_user(person_dto)

    @app.route('/users/<int:person_id>', methods=['PUT'])
    def update_person_route(person_id):
        data = request.get_json()
        update_person_dto = UpdatePersonDTO(data['first_name'], data['last_name'], data['age'])
        return update_user(person_id, update_person_dto)

    @app.route('/users/<int:person_id>', methods=['DELETE'])
    def delete_person_route(person_id):
        return delete_user(person_id)