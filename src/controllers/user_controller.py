from flask import jsonify
from database.db import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text

#DTOS
from dtos.user.create_user_dto import UserDTO
from dtos.user.update_user_dto import UpdateUserDTO

def get_all_users():
    try:
        with db.engine.connect() as connection:
            sql = text('SELECT * FROM user')
            result = connection.execute(sql)
            users = result.fetchall()

        service_orders_list = [dict(row._mapping) for row in users]

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


def get_user_by_id(id):
    try:
        with db.engine.connect() as connection:
            sql = text('SELECT * FROM user WHERE id = :id')
            result = connection.execute(sql, {'id': id})
            user = result.fetchone()

        if user:
            return jsonify({
                "success": True,
                "user": dict(user._mapping)
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": "Usuário não encontrado"
            }), 404

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    
    
def create_user(create_user_dto: UserDTO):
    try:
        with db.engine.connect() as connection:
            sql = text('INSERT INTO user (first_name, last_name, age, password) VALUES (:first_name, :last_name, :age, :password)')
            connection.execute(sql, {
                'first_name': create_user_dto.first_name,
                'last_name': create_user_dto.last_name,
                'age': create_user_dto.age,
                'password': create_user_dto.password
            })
            connection.commit()

        return jsonify({
            "success": True,
            "message": "Usuário criado com sucesso"
        }), 201

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    

def update_user(id, update_user_dto: UpdateUserDTO):
    try:
        with db.engine.connect() as connection:

            sql = text('UPDATE user SET first_name = :first_name, last_name = :last_name, age = :age, password = :password WHERE id = :id')
            result= connection.execute(sql, {
                'id': id,
                'first_name': update_user_dto.first_name,
                'last_name': update_user_dto.last_name,
                'age': update_user_dto.age,
                'password': update_user_dto.password
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
    
    
def delete_user(id):
    try:
        with db.engine.connect() as connection:

            sql = text('DELETE FROM user WHERE id = :id')
            result= connection.execute(sql, {'id':id})

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