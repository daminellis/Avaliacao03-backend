from flask import jsonify
from database.db import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text

#DTOS
from dtos.notebook.create_notebook_dto import NotebookDTO
from dtos.notebook.update_notebook_dto import UpdateNotebookDTO

def get_all_notebooks():
    try:
        with db.engine.connect() as connection:
            sql = text("SELECT * FROM notebook")
            result = connection.execute(sql)
            service_orders = result.fetchall()
            
            service_orders_list = [dict(row._mapping) for row in service_orders]

            if service_orders_list:
                return jsonify({
                    "success": True,
                    "notebooks": service_orders_list
                }), 200
            else:
                return jsonify({
                    "success": False,
                    "error": "Notas não encontradas ou nenhuma nota cadastrada"
                }), 404
            
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500


def get_notebook_by_id(notebook_id):
    try:
        with db.engine.connect() as connection:

            sql = text("SELECT * FROM notebook WHERE notebook_id = :notebook_id")
            result = connection.execute(sql, {'notebook_id':notebook_id})
            notebook = result.fetchone()

            if notebook:
                return jsonify({
                    "success": True,
                    "notebook": dict(notebook._mapping)
                }), 200
            else:
                return jsonify({
                    "success": False,
                    "error": "Nota não encontrada ou não cadastrada"
                }), 404
        
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500


def create_notebook(notebook_dto: NotebookDTO):
    try:
        with db.engine.connect() as connection:
            sql = text("INSERT INTO notebook (Note_Title, Med_Name, Med_Desc, Med_Method, Med_Type, Med_Freq, Qtd_Taken, Qtd_Total, Init_Schedule, End_Schedule, status, Obs, Person_Id) VALUES (:Note_Title, :Med_Name, :Med_Desc, :Med_Method, :Med_Type, :Med_Freq, :Qtd_Taken, :Qtd_Total, :Init_Schedule, :End_Schedule, :status, :Obs, :Person_Id)")
            connection.execute(sql, {
                "Note_Title": notebook_dto.title,
                "Med_Name": notebook_dto.med_name,
                "Med_Desc": notebook_dto.description,
                "Med_Method": notebook_dto.method,
                "Med_Type": notebook_dto.med_type,
                "Med_Freq": notebook_dto.med_freq,
                "Qtd_Taken": notebook_dto.qtd_taken,
                "Qtd_Total": notebook_dto.qtd_total,
                "Init_Schedule": notebook_dto.init_schedule,
                "End_Schedule": notebook_dto.end_schedule,
                "status": notebook_dto.status,
                "Obs": notebook_dto.obs,
                "Person_Id": notebook_dto.person_id
            })
            connection.commit()

            return jsonify({
                "success": True,
                "message": "Nota criada com sucesso"
            }), 201
        
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500


def update_notebook(notebook_id, notebook_dto: UpdateNotebookDTO):
    try:
        with db.engine.connect() as connection:
            sql = text("UPDATE notebook SET Note_Title = :Note_Title, Med_Name = :Med_Name, Med_Desc = :Med_Desc, Med_Method = :Med_Method, Med_Type = :Med_Type, Med_Freq = :Med_Freq, Qtd_Taken = :Qtd_Taken, Qtd_Total = :Qtd_Total, Init_Schedule = :Init_Schedule, End_Schedule = :End_Schedule, status = :status, Obs = :Obs, Person_Id = :Person_Id WHERE notebook_id = :notebook_id")
            result= connection.execute(sql, {
                "notebook_id": notebook_id,
                "Note_Title": notebook_dto.title,
                "Med_Name": notebook_dto.med_name,
                "Med_Desc": notebook_dto.description,
                "Med_Method": notebook_dto.method,
                "Med_Type": notebook_dto.med_type,
                "Med_Freq": notebook_dto.med_freq,
                "Qtd_Taken": notebook_dto.qtd_taken,
                "Qtd_Total": notebook_dto.qtd_total,
                "Init_Schedule": notebook_dto.init_schedule,
                "End_Schedule": notebook_dto.end_schedule,
                "status": notebook_dto.status,
                "Obs": notebook_dto.obs,
                "Person_Id": notebook_dto.person_id
            })

            if result.rowcount == 0:
                return jsonify({
                    "success": False,
                    "error": "Nota não encontrada"
                }), 404

            connection.commit()

            return jsonify({
                "success": True,
                "message": "Nota atualizada com sucesso"
            }), 200
        
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500


def delete_notebook(notebook_id):
    try:
        with db.engine.connect() as connection:
            sql = text("DELETE FROM notebook WHERE id = :id")
            result= connection.execute(sql, {'notebok_id':notebook_id})
            
            if result.rowcount == 0:
                return jsonify({
                    "success": False,
                    "error": "Nota não encontrada"
                }), 404
            
            connection.commit()

            return jsonify({
                "success": True,
                "message": "Nota deletada com sucesso"
            }), 200
        
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500