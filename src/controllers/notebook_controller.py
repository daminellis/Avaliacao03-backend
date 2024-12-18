from services.notebook_service import get_all_notebooks
from services.notebook_service import get_notebook_by_id
from services.notebook_service import create_notebook
from services.notebook_service import update_notebook
from services.notebook_service import delete_notebook

from flask import request
from flask_jwt_extended import jwt_required

#Repository
# from repositories.notebook.create_notebook_repository import NotebookRepository
# from repositories.notebook.update_notebook_repository import UpdateNotebookRepository

#DTO
from dtos.notebook.create_notebook_dto import CreateNotebookDTO
from dtos.notebook.update_notebook_dto import UpdateNotebookDTO

def notebook(app):
    @app.route('/notebooks', methods=['GET'])
    @jwt_required()
    def get_all_notebooks_route():
        return get_all_notebooks()
    
    @app.route('/notebooks/<int:id>', methods=['GET'])
    @jwt_required()
    def get_notebook_by_id_route(id):
        return get_notebook_by_id(id)
    
    @app.route('/notebook', methods=['POST'])
    @jwt_required()
    def create_notebook_route():
        data= request.get_json()
        create_notebook_dto= CreateNotebookDTO(data['note_title'], data['med_stock_id'], data['note_desc'], data['med_method'], data['med_type'], data['med_freq'], data['qtd_taken'], data['qtd_total'], data['init_schedule'], data['end_schedule'], data['status'], data['obs'], data['user_id'])
        return create_notebook(create_notebook_dto)

    @app.route('/notebooks/<int:id>', methods=['PATCH'])
    @jwt_required()
    def update_notebook_route(id):
        data= request.get_json()
        update_notebook_dto= UpdateNotebookDTO(data['note_title'], data['med_stock_id'], data['note_desc'], data['med_method'], data['med_type'], data['med_freq'], data['qtd_taken'], data['qtd_total'], data['init_schedule'], data['end_schedule'], data['status'], data['obs'], data['user_id'])
        return update_notebook(id ,update_notebook_dto)

    @app.route('/notebooks/<int:id>', methods=['DELETE'])
    @jwt_required()
    def delete_notebook_route(id):
        return delete_notebook(id)