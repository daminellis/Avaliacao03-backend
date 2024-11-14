from flask import jsonify
from database.db import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text

#Repository
# from repositories.user.create_user_repository import UserRepository
# from repositories.user.update_user_repository import UpdateUserRepository

#DTO
from dtos.user.create_user_dto import CreateUserDTO
from dtos.user.update_user_dto import UpdateUserDTO
from dtos.responses.success.success_dto import SuccessDTO
from dtos.responses.error.error_dto import ErrorDTO

def get_all_users():
    try:
        with db.engine.connect() as connection:
            sql = text('SELECT * FROM user')
            result = connection.execute(sql)
            users = result.fetchall()

        service_orders_list = [dict(row._mapping) for row in users]

        if service_orders_list:
            return jsonify(SuccessDTO(code=200, data=service_orders_list)), 200
        else:
            return jsonify(ErrorDTO(code=404, message="Nenhum usuário cadastrado no banco", details=['path: GET /users'])), 404

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
            return jsonify(SuccessDTO(code=200, data=user)), 200
        else:
            return jsonify(ErrorDTO(code=404, message="Usuário não encontrado", details=['path: GET /users/<:id>'])), 404

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    
def get_user_by_first_name(first_name):
    try:
        with db.engine.connect() as connection:
            sql = text('SELECT * FROM user WHERE first_name = :first_name')
            result = connection.execute(sql, {'first_name': first_name})
            user = result.fetchone()

        if user:
            return jsonify(SuccessDTO(code=200, data=user)), 200
        else:
            return jsonify(ErrorDTO(code=404, message="Usuário não encontrado", details=['path: GET /users/<:first_name>'])), 404

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500


def create_user(create_user_dto: CreateUserDTO):
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

        return jsonify(SuccessDTO(code=201, message="Usuário criado com sucesso")), 201

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
                return jsonify(ErrorDTO(code=404, message="Usuário não encontrado", details=['path: PATCH /users/<:id>'])), 404            
            connection.commit()

        return jsonify(SuccessDTO(code=200, message="Usuário atualizado com sucesso")), 200
    
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    
    
def delete_user(id):
    try:
        with db.engine.connect() as connection:

            sql = text('DELETE FROM user WHERE id = :id')
            result= connection.execute(sql, {'id':id})

            if result.rowcount == 0:
                return jsonify(ErrorDTO(code=404, message="Usuário não encontrado", details=['path: DELETE /users/<:id>'])), 404
            connection.commit()

        return jsonify(SuccessDTO(code=200, message="Usuário deletado com sucesso")), 200

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500