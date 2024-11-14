from flask import jsonify
from database.db import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text

#Repository
# from repositories.notebook.create_notebook_repository import NotebookRepository
# from repositories.notebook.update_notebook_repository import UpdateNotebookRepository

#DTO
from dtos.notebook.create_notebook_dto import CreateNotebookDTO
from dtos.notebook.update_notebook_dto import UpdateNotebookDTO
from dtos.responses.success.success_dto import SuccessDTO
from dtos.responses.error.error_dto import ErrorDTO

def get_all_notebooks():
    try:
        with db.engine.connect() as connection:
            sql = text("SELECT * FROM notebook")
            result = connection.execute(sql)
            notes = result.fetchall()
            
            service_orders_list = [dict(row._mapping) for row in notes]

            if service_orders_list:
                return jsonify(SuccessDTO(code=200, data=service_orders_list)), 200
            else:
                return jsonify(ErrorDTO(code=404, message="Notas não encontradas ou nenhuma nota cadastrada", details=['path: GET /notebooks'])), 404
            
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500


def get_notebook_by_id(id):
    try:
        with db.engine.connect() as connection:

            sql = text("SELECT * FROM notebook WHERE id = :id")
            result = connection.execute(sql, {'id':id})
            note = result.fetchone()

            if note:
                return jsonify(SuccessDTO(code=200, data=note)), 200
            else:
                return jsonify(ErrorDTO(code=404, message="Nota não encontrada", details=['path: GET /notebooks/<:id>'])), 404
            
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500


def create_notebook(create_notebook_dto: CreateNotebookDTO):
    try:
        with db.engine.connect() as connection:
            sql = text("INSERT INTO notebook (note_title, med_stock_id, note_desc, med_method, med_type, med_freq, qtd_taken, qtd_total, init_schedule, end_schedule, status, obs, user_id) VALUES (:note_title, :med_stock_id, :note_desc, :med_method, :med_type, :med_freq, :qtd_taken, :qtd_total, :init_schedule, :end_schedule, :status, :obs, :user_id)")
            connection.execute(sql, {
                "note_title": create_notebook_dto.note_title,
                "med_stock_id": create_notebook_dto.med_stock_id,
                "note_desc": create_notebook_dto.note_desc,
                "med_method": create_notebook_dto.med_method,
                "med_type": create_notebook_dto.med_type,
                "med_freq": create_notebook_dto.med_freq,
                "qtd_taken": create_notebook_dto.qtd_taken,
                "qtd_total": create_notebook_dto.qtd_total,
                "init_schedule": create_notebook_dto.init_schedule,
                "end_schedule": create_notebook_dto.end_schedule,
                "status": create_notebook_dto.status,
                "obs": create_notebook_dto.obs,
                "user_id": create_notebook_dto.user_id
            })
            connection.commit()

            return jsonify(SuccessDTO(code=200, message="Nota adicionada com sucesso")), 200
        
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500


def update_notebook(id, update_notebook_dto: UpdateNotebookDTO):
    try:
        with db.engine.connect() as connection:
            sql = text("UPDATE notebook SET note_title = :note_title, med_stock_id = :med_stock_id, note_desc = :note_desc, med_method = :med_method, med_type = :med_type, med_freq = :med_freq, qtd_taken = :qtd_taken, qtd_total = :qtd_total, init_schedule = :init_schedule, end_schedule = :end_schedule, status = :status, obs = :obs, user_id = :user_id WHERE id = :id")
            result= connection.execute(sql, {
               "id": id,
                "note_title": update_notebook_dto.note_title,
                "med_stock_id": update_notebook_dto.med_stock_id,
                "note_desc": update_notebook_dto.note_desc,
                "med_method": update_notebook_dto.med_method,
                "med_type": update_notebook_dto.med_type,
                "med_freq": update_notebook_dto.med_freq,
                "qtd_taken": update_notebook_dto.qtd_taken,
                "qtd_total": update_notebook_dto.qtd_total,
                "init_schedule": update_notebook_dto.init_schedule,
                "end_schedule": update_notebook_dto.end_schedule,
                "status": update_notebook_dto.status,
                "obs": update_notebook_dto.obs,
                "user_id": update_notebook_dto.user_id
            })

            if result.rowcount == 0:
                return jsonify(ErrorDTO(code=404, message="Nota não encontrada", details=['path: PUT /notebooks/<:id>'])), 404

            connection.commit()

            return jsonify(SuccessDTO(code=200, message="Nota atualizada com sucesso")), 200
        
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500


def delete_notebook(id):
    try:
        with db.engine.connect() as connection:
            sql = text("DELETE FROM notebook WHERE id = :id")
            result= connection.execute(sql, {'id':id})
            
            if result.rowcount == 0:
                return jsonify(ErrorDTO(code=404, message="Nota não encontrada", details=['path: DELETE /notebooks/<:id>'])), 404
            
            connection.commit()

            return jsonify(SuccessDTO(code=200, message="Nota deletada com sucesso")), 200
                
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500