from controllers.persons_controller import get_all_persons
from controllers.persons_controller import get_person_by_id
from controllers.persons_controller import create_person
from controllers.persons_controller import update_person
from controllers.persons_controller import delete_person
from flask import request

from dtos.person.create_person_dto import PersonDTO
from dtos.person.update_person_dto import UpdatePersonDTO

def persons(app):
    @app.route('/allpersons', methods=['GET'])
    def get_all_persons_route():
        return get_all_persons()

    @app.route('/persons/<int:person_id>', methods=['GET'])
    def get_person_by_id_route(person_id):
        return get_person_by_id(person_id)

    @app.route('/createperson', methods=['POST'])
    def create_person_route():
        data = request.get_json()
        person_dto = PersonDTO(data['first_name'], data['last_name'], data['age'])
        return create_person(person_dto)

    @app.route('/updateperson/<int:person_id>', methods=['PUT'])
    def update_person_route(person_id):
        data = request.get_json()
        update_person_dto = UpdatePersonDTO(data['first_name'], data['last_name'], data['age'])
        return update_person(person_id, update_person_dto)

    @app.route('/deleteperson/<int:person_id>', methods=['DELETE'])
    def delete_person_route(person_id):
        return delete_person(person_id)