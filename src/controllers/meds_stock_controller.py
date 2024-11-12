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
            sql = text('SELECT * FROM meds_stock')
            result = connection.execute(sql)
            meds_stock = result.fetchall()

        meds_stock_list = [dict(row._mapping) for row in meds_stock]

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
    
def get_meds_stock_by_id(meds_stock_id):
    try:
        with db.engine.connect() as connection:
            sql = text('SELECT * FROM meds_stock WHERE meds_stock_id = :meds_stock_id')
            result = connection.execute(sql, {'meds_stock_id':meds_stock_id})
            meds_stock = result.fetchone()

        if meds_stock:
            return jsonify({
                "success": True,
                "meds_stock": dict(meds_stock._mapping)
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": "Medicamento não encontrado no estoque"
            }), 404

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    

def create_meds_stock(meds_stock_dto: MedsStockDTO):
    try:
        with db.engine.connect() as connection:
            sql = text('INSERT INTO meds_stock (Meds_Name, Meds_Qtd, Meds_val, Meds_Desc, Meds_Type, Required_Person) VALUES (:meds_name, :meds_qtd, :meds_val, :mds_desc, :meds_type, :person_id)')
            connection.execute(sql, {
                "meds_name": meds_stock_dto.meds_name,
                "meds_qtd": meds_stock_dto.meds_qtd,
                "meds_val": meds_stock_dto.meds_val,
                "mds_desc": meds_stock_dto.mds_desc,
                "meds_type": meds_stock_dto.meds_type,
                "person_id": meds_stock_dto.person_id
            })
            connection.commit()
            return jsonify({
                "success": True,
                "message": "Medicamento adicionado ao estoque"
            }), 201

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500


def update_meds_stock(id, meds_stock_dto: UpdateMedsStockDTO):
    try:
        with db.engine.connect() as connection:
            sql = text('UPDATE meds_stock SET Meds_Name = :meds_name, Meds_Qtd = :meds_qtd, Meds_val = :meds_val, Meds_Desc = :mds_desc, Meds_Type = :meds_type, Required_Person = :person_id WHERE id = :meds_stock_id')
            result= connection.execute(sql, {
                "meds_stock_id": id,
                "meds_name": meds_stock_dto.meds_name,
                "meds_qtd": meds_stock_dto.meds_qtd,
                "meds_val": meds_stock_dto.meds_val,
                "mds_desc": meds_stock_dto.mds_desc,
                "meds_type": meds_stock_dto.meds_type,
                "person_id": meds_stock_dto.person_id
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
    
def delete_meds_stock(meds_stock_id):
    try:
        with db.engine.connect() as connection:
            sql = text('DELETE FROM meds_stock WHERE meds_stock_id = :meds_stock_id')
            result= connection.execute(sql, {'meds_stock_id':meds_stock_id})
            
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