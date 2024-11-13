from flask import jsonify
from database.db import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text

#DTOS
from dtos.meds_stock.create_meds_stock_dto import MedsStockDTO
from dtos.meds_stock.update_meds_stock_dto import UpdateMedsStockDTO

def get_all_meds_stock():
    try:
        with db.engine.connect() as connection:
            sql = text('SELECT * FROM med_stock')
            result = connection.execute(sql)
            stock = result.fetchall()

        meds_stock_list = [dict(row._mapping) for row in stock]

        if meds_stock_list:
            return jsonify({
                "success": True,
                "meds_stock": meds_stock_list
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": "Estoque de medicamentos não encontrado"
            }), 404

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    
def get_meds_stock_by_id(id):
    try:
        with db.engine.connect() as connection:
            sql = text('SELECT * FROM med_stock WHERE id = :id')
            result = connection.execute(sql, {'id':id})
            med = result.fetchone()

        if med:
            return jsonify({
                "success": True,
                "meds_stock": dict(med._mapping)
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": "Medicamento não encontrado no estoque"
            }), 404

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    

def create_meds_stock(create_meds_stock_dto: MedsStockDTO):
    try:
        with db.engine.connect() as connection:
            sql = text('INSERT INTO med_stock (med_name, med_qtd, med_val, med_desc, med_type, user_id) VALUES (:med_name, :med_qtd, :med_val, :med_desc, :med_type, :user_id)')
            connection.execute(sql, {
                "med_name": create_meds_stock_dto.med_name,
                "med_qtd": create_meds_stock_dto.med_qtd,
                "med_val": create_meds_stock_dto.med_val,
                "med_desc": create_meds_stock_dto.med_desc,
                "med_type": create_meds_stock_dto.med_type,
                "user_id": create_meds_stock_dto.user_id
            })
            connection.commit()
            return jsonify({
                "success": True,
                "message": "Medicamento adicionado ao estoque"
            }), 201

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500


def update_meds_stock(id, update_meds_stock_dto: UpdateMedsStockDTO):
    try:
        with db.engine.connect() as connection:
            sql = text('UPDATE med_stock SET med_name = :med_name, med_qtd = :med_qtd, med_val = :med_val, med_desc = :med_desc, med_type = :med_type, user_id = :user_id WHERE id = :id')
            result= connection.execute(sql, {
                "id": id,
                "med_name": update_meds_stock_dto.med_name,
                "med_qtd": update_meds_stock_dto.med_qtd,
                "med_val": update_meds_stock_dto.med_val,
                "med_desc": update_meds_stock_dto.med_desc,
                "med_type": update_meds_stock_dto.med_type,
                "user_id": update_meds_stock_dto.user_id
            })

            if result.rowcount == 0:
                return jsonify({
                    "success": False,
                    "error": "Medicamento não encontrado"
                }), 404
            
            connection.commit()

            return jsonify({
                "success": True,
                "message": "Medicamento atualizado"
            }), 200

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    
def delete_meds_stock(id):
    try:
        with db.engine.connect() as connection:
            sql = text('DELETE FROM med_stock WHERE id = :id')
            result= connection.execute(sql, {'id': id})
            
            if result.rowcount == 0:
                return jsonify({
                    "success": False,
                    "error": "Medicamento não encontrado"
                }), 404

            connection.commit()
            return jsonify({
                "success": True,
                "message": "Medicamento deletado"
            }), 200

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500