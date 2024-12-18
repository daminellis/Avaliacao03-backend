from flask import jsonify
from database.db import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text
from utils.functions.dateformatter import date_formatter
from datetime import datetime

#Repository
# from repositories.meds_stock.create_meds_stock_repository import MedsStockRepository
# from repositories.meds_stock.update_meds_stock_repository import UpdateMedsStockRepository

#DTO
from dtos.meds_stock.create_med_stock_dto import CreateMedStockDTO
from dtos.meds_stock.update_med_stock_dto import UpdateMedStockDTO
from dtos.responses.success.success_dto import SuccessDTO
from dtos.responses.error.error_dto import ErrorDTO

def get_all_meds_stock():
    try:
        with db.engine.connect() as connection:
            sql = text('SELECT * FROM med_stock')
            result = connection.execute(sql)
            stock = result.fetchall()

        meds_stock_list = [dict(row._mapping) for row in stock]

        if meds_stock_list:
            return jsonify(SuccessDTO(code=200, data=meds_stock_list)), 200
        else:
            return jsonify(ErrorDTO(code=404, message="Nenhum medicamento cadastrado no estoque", details=['path: GET /meds_stock'])), 404

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
            return jsonify(SuccessDTO(code=200, data=med)), 200
        else:
            return jsonify(ErrorDTO(code=404, message="Medicamento não encontrado", details=['path: GET /meds_stock/<:id>'])), 404

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    

def create_meds_stock(create_meds_stock_dto: CreateMedStockDTO):
    try:
        with db.engine.connect() as connection:
            sql = text('INSERT INTO med_stock (med_name, med_qtd, med_val, med_desc, med_type, user_id) VALUES (:med_name, :med_qtd, :med_val, :med_desc, :med_type, :user_id)')
            connection.execute(sql, {
                "med_name": create_meds_stock_dto.med_name,
                "med_qtd": create_meds_stock_dto.med_qtd,
                "med_val": date_formatter(create_meds_stock_dto.med_val),
                "med_desc": create_meds_stock_dto.med_desc,
                "med_type": create_meds_stock_dto.med_type,
                "user_id": create_meds_stock_dto.user_id
            })

            current_date = datetime.now().date()
            med_val_date = datetime.strptime(create_meds_stock_dto.med_val, '%d/%m/%Y').date()

            if med_val_date < current_date:
                return jsonify(ErrorDTO(code=400, message="Data de validade inválida. Medicações vencidas não podem ser cadastradas!", details=['path: POST /meds_stock'])), 400

            connection.commit()
            return jsonify(SuccessDTO(code=201, message="Medicamento adicionado ao estoque.")), 201

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500


def update_meds_stock(id, update_meds_stock_dto: UpdateMedStockDTO):
    try:
        with db.engine.connect() as connection:
            sql = text('UPDATE med_stock SET med_name = :med_name, med_qtd = :med_qtd, med_val = :med_val, med_desc = :med_desc, med_type = :med_type, user_id = :user_id WHERE id = :id')
            result= connection.execute(sql, {
                "id": id,
                "med_name": update_meds_stock_dto.med_name,
                "med_qtd": update_meds_stock_dto.med_qtd,
                "med_val": date_formatter(update_meds_stock_dto.med_val),
                "med_desc": update_meds_stock_dto.med_desc,
                "med_type": update_meds_stock_dto.med_type,
                "user_id": update_meds_stock_dto.user_id
            })

            current_date = datetime.now().date()

            med_val_date = datetime.strptime(update_meds_stock_dto.med_val, '%d/%m/%Y').date()

            if med_val_date < current_date:
                return jsonify(ErrorDTO(code=400, message="Data de validade inválida. Medicações vencidas não podem ser atualizadas!", details=['path: PUT /meds_stock/<:id>'])), 400

    
            if result.rowcount == 0:
                return jsonify(ErrorDTO(code=404, message="Medicamento não encontrado", details=['path: PUT /meds_stock/<:id>'])), 404

            connection.commit()

            return jsonify(SuccessDTO(code=200, message="Medicamento atualizado")), 200
        
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500
    
def delete_meds_stock(id):
    try:
        with db.engine.connect() as connection:
            sql = text('DELETE FROM med_stock WHERE id = :id')
            result= connection.execute(sql, {'id': id})
            
            if result.rowcount == 0:
                return jsonify(ErrorDTO(code=404, message="Medicamento não encontrado", details=['path: DELETE /meds_stock/<:id>'])), 404

            connection.commit()
            return jsonify(SuccessDTO(code=200, message="Medicamento deletado")), 200

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500