from flask import jsonify
from database.db import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text

#DTOS
from dtos.person.create_person_dto import PersonDTO
from dtos.person.update_person_dto import UpdatePersonDTO

def get_all_users():
    try:
        with db.engine.connect() as connection:
            sql = text('SELECT * FROM persons')
            result = connection.execute(sql)
            service_orders = result.fetchall()

        service_orders_list = [dict(row._mapping) for row in service_orders]

        if service_orders_list:
            return jsonify({
                "success": True,
                "service_orders": service_orders_list
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": "Usuários não encontrados"
            }), 404

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500


def get_user_by_id(person_id):
    try:
        with db.engine.connect() as connection:
            sql = text('SELECT * FROM persons WHERE person_id = :person_id')
            result = connection.execute(sql, {'person_id': person_id})
            person = result.fetchone()

        if person:
            return jsonify({
                "success": True,
                "person": dict(person._mapping)
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": "Usuário não encontrado"
            }), 404

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    
    
def create_user(person_dto: PersonDTO):
    try:
        with db.engine.connect() as connection:
            sql = text('INSERT INTO persons (First_Name, Last_Name, Age) VALUES (:First_Name, :Last_Name, :Age)')
            connection.execute(sql, {
                'First_Name': person_dto.first_name,
                'Last_Name': person_dto.last_name,
                'Age': person_dto.age
            })
            connection.commit()

        return jsonify({
            "success": True,
            "message": "Usuário criado com sucesso"
        }), 201

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    

def update_user(person_id, person_dto: UpdatePersonDTO):
    try:
        with db.engine.connect() as connection:

            sql = text('UPDATE persons SET First_Name = :First_Name, Last_Name = :Last_Name, Age = :Age WHERE person_id = :person_id')
            result= connection.execute(sql, {
                'person_id': person_id,
                'First_Name': person_dto.first_name,
                'Last_Name': person_dto.last_name,
                'Age': person_dto.age
            })

            if result.rowcount == 0:
                return jsonify({
                    "success": False,
                    "error": "Usuário não encontrado"
                }), 404
            
            connection.commit()

        return jsonify({
            "success": True,
            "message": "Usuário atualizado com sucesso"
        }), 200

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    
    
def delete_user(person_id):
    try:
        with db.engine.connect() as connection:

            sql = text('DELETE FROM persons WHERE person_id = :person_id')
            result= connection.execute(sql, {'person_id':person_id})

            if result.rowcount == 0:
                return jsonify({
                    "success": False,
                    "error": "Usuário não encontrado"
                }), 404
            
            connection.commit()

        return jsonify({
            "success": True,
            "message": "Usuário deletado com sucesso"
        }), 200

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500