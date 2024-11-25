from datetime import date, datetime
from flask import jsonify
from database.db import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text
from utils.functions.timestamp_formatter import timestamp_formatter

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
            stock_check_sql = text("SELECT med_qtd FROM med_stock WHERE id = :med_stock_id")
            stock_result = connection.execute(stock_check_sql, {"med_stock_id": create_notebook_dto.med_stock_id}).fetchone()
            
            if stock_result is None:
                return jsonify(ErrorDTO(code=404, message="Medicamento não encontrado no estoque", details=['path: POST /notebook'])), 404
            
            med_qtd = stock_result[0]
            
            if create_notebook_dto.qtd_total != med_qtd:
                return jsonify(ErrorDTO(code=400, message="qtd_total não bate com med_qtd no estoque", details=['path: POST /notebook'])), 400
            
            stock_check_med_val_sql = text("SELECT med_val FROM med_stock WHERE id = :med_stock_id")
            stock_med_val_result = connection.execute(
                stock_check_med_val_sql, {"med_stock_id": create_notebook_dto.med_stock_id}
            ).fetchone()

            if not stock_med_val_result:
                return jsonify(ErrorDTO(code=404, message="Medicamento não encontrado no estoque", details=['path: POST /notebook'])), 404

            med_val_date = stock_med_val_result[0]
            if not isinstance(med_val_date, (datetime, date)):
                return jsonify(ErrorDTO(code=500, message="Data de validade do medicamento inválida", details=['path: POST /notebook'])), 500

            if isinstance(med_val_date, datetime):
                med_val_date = med_val_date.date()

            
            current_date = datetime.now().date()

            if med_val_date < current_date:
                return jsonify(ErrorDTO(code=400, message="Data de validade do medicamento expirada. O tratamento não pode ser iniciado", details=['path: POST /notebook'])), 400
            

            try:
                init_schedule_date = (
                    datetime.strptime(create_notebook_dto.init_schedule, '%d/%m/%Y %H:%M:%S').date()
                    if isinstance(create_notebook_dto.init_schedule, str)
                    else create_notebook_dto.init_schedule
                )
                end_schedule_date = (
                    datetime.strptime(create_notebook_dto.end_schedule, '%d/%m/%Y %H:%M:%S').date()
                    if isinstance(create_notebook_dto.end_schedule, str)
                    else create_notebook_dto.end_schedule
                )
            except ValueError:
                return jsonify(ErrorDTO(code=400, message="Formato de data inválido", details=['path: POST /notebook'])), 400

            if init_schedule_date > med_val_date:
                return jsonify(ErrorDTO(code=400, message="A data de início do tratamento é maior que a validade do medicamento. O tratamento não pode ser iniciado", details=['path: POST /notebook'])), 400

            if end_schedule_date > med_val_date:
                return jsonify(ErrorDTO(code=400, message="A data de término do tratamento é maior que a validade do medicamento. O tratamento não pode ser iniciado", details=['path: POST /notebook'])), 400

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
                "init_schedule": timestamp_formatter(create_notebook_dto.init_schedule),
                "end_schedule": timestamp_formatter(create_notebook_dto.end_schedule),
                "status": create_notebook_dto.status,
                "obs": create_notebook_dto.obs,
                "user_id": create_notebook_dto.user_id
            })

            new_med_qtd = med_qtd - create_notebook_dto.qtd_taken
            update_stock_sql = text("UPDATE med_stock SET med_qtd = :new_med_qtd WHERE id = :med_stock_id")
            connection.execute(update_stock_sql, {"new_med_qtd": new_med_qtd, "med_stock_id": create_notebook_dto.med_stock_id})
            connection.commit()

            return jsonify(SuccessDTO(code=200, message="Nota adicionada com sucesso")), 200
        
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return jsonify({'error': error}), 500


def update_notebook(id, update_notebook_dto: UpdateNotebookDTO):
    try:
        with db.engine.connect() as connection:
            stock_check_sql = text("SELECT med_qtd, med_val FROM med_stock WHERE id = :med_stock_id")
            stock_result = connection.execute(stock_check_sql, {"med_stock_id": update_notebook_dto.med_stock_id}).fetchone()

            if stock_result is None:
                return jsonify(ErrorDTO(code=404, message="Medicamento não encontrado no estoque", details=['path: PATCH /notebooks/<:id>'])), 404

            med_qtd, med_val_date = stock_result

            if update_notebook_dto.qtd_total != med_qtd:
                return jsonify(ErrorDTO(code=400, message="qtd_total não bate com med_qtd no estoque", details=['path: PATCH /notebooks/<:id>'])), 400

            if not isinstance(med_val_date, (datetime, date)):
                return jsonify(ErrorDTO(code=500, message="Data de validade do medicamento inválida", details=['path: PATCH /notebooks/<:id>'])), 500

            if isinstance(med_val_date, datetime):
                med_val_date = med_val_date.date()

            current_date = datetime.now().date()

            if med_val_date < current_date:
                return jsonify(ErrorDTO(code=400, message="Data de validade do medicamento expirada. O tratamento não pode ser iniciado", details=['path: PATCH /notebooks/<:id>'])), 400

            try:
                init_schedule_date = (
                    datetime.strptime(update_notebook_dto.init_schedule, '%d/%m/%Y %H:%M:%S').date()
                    if isinstance(update_notebook_dto.init_schedule, str)
                    else update_notebook_dto.init_schedule
                )
                end_schedule_date = (
                    datetime.strptime(update_notebook_dto.end_schedule, '%d/%m/%Y %H:%M:%S').date()
                    if isinstance(update_notebook_dto.end_schedule, str)
                    else update_notebook_dto.end_schedule
                )
            except ValueError:
                return jsonify(ErrorDTO(code=400, message="Formato de data inválido", details=['path: PATCH /notebooks/<:id>'])), 400

            if init_schedule_date > med_val_date:
                return jsonify(ErrorDTO(code=400, message="A data de início do tratamento é maior que a validade do medicamento. O tratamento não pode ser iniciado", details=['path: PATCH /notebooks/<:id>'])), 400

            if end_schedule_date > med_val_date:
                return jsonify(ErrorDTO(code=400, message="A data de término do tratamento é maior que a validade do medicamento. O tratamento não pode ser iniciado", details=['path: PATCH /notebooks/<:id>'])), 400

            sql = text("UPDATE notebook SET note_title = :note_title, med_stock_id = :med_stock_id, note_desc = :note_desc, med_method = :med_method, med_type = :med_type, med_freq = :med_freq, qtd_taken = :qtd_taken, qtd_total = :qtd_total, init_schedule = :init_schedule, end_schedule = :end_schedule, status = :status, obs = :obs, user_id = :user_id WHERE id = :id")
            result = connection.execute(sql, {
                "id": id,
                "note_title": update_notebook_dto.note_title,
                "med_stock_id": update_notebook_dto.med_stock_id,
                "note_desc": update_notebook_dto.note_desc,
                "med_method": update_notebook_dto.med_method,
                "med_type": update_notebook_dto.med_type,
                "med_freq": update_notebook_dto.med_freq,
                "qtd_taken": update_notebook_dto.qtd_taken,
                "qtd_total": update_notebook_dto.qtd_total,
                "init_schedule": timestamp_formatter(update_notebook_dto.init_schedule),
                "end_schedule": timestamp_formatter(update_notebook_dto.end_schedule),
                "status": update_notebook_dto.status,
                "obs": update_notebook_dto.obs,
                "user_id": update_notebook_dto.user_id
            })

            if result.rowcount == 0:
                return jsonify(ErrorDTO(code=404, message="Nota não encontrada", details=['path: PUT /notebooks/<:id>'])), 404

            new_med_qtd = med_qtd - update_notebook_dto.qtd_taken
            update_stock_sql = text("UPDATE med_stock SET med_qtd = :new_med_qtd WHERE id = :med_stock_id")
            connection.execute(update_stock_sql, {"new_med_qtd": new_med_qtd, "med_stock_id": update_notebook_dto.med_stock_id})
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