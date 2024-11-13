from controllers.notebook_controller import get_all_notebooks
from controllers.notebook_controller import get_notebook_by_id
from controllers.notebook_controller import create_notebook
from controllers.notebook_controller import update_notebook
from controllers.notebook_controller import delete_notebook
from flask import request

#DTOS
from dtos.notebook.create_notebook_dto import NotebookDTO
from dtos.notebook.update_notebook_dto import UpdateNotebookDTO

def notebook(app):
    @app.route('/notebooks', methods=['GET'])
    def get_all_notebooks_route():
        return get_all_notebooks()
    
    @app.route('/notebooks/<int:id>', methods=['GET'])
    def get_notebook_by_id_route(id):
        return get_notebook_by_id(id)
    
    @app.route('/notebook', methods=['POST'])
    def create_notebook_route():
        data= request.get_json()
        create_notebook_dto= NotebookDTO(data['note_title'], data['med_stock_id'], data['note_desc'], data['med_method'], data['med_type'], data['med_freq'], data['qtd_taken'], data['qtd_total'], data['init_schedule'], data['end_schedule'], data['status'], data['obs'], data['user_id'])
        return create_notebook(create_notebook_dto)

    @app.route('/notebooks/<int:id>', methods=['PUT'])
    def update_notebook_route(id):
        data= request.get_json()
        update_notebook_dto= UpdateNotebookDTO(data['note_title'], data['med_stock_id'], data['note_desc'], data['med_method'], data['med_type'], data['med_freq'], data['qtd_taken'], data['qtd_total'], data['init_schedule'], data['end_schedule'], data['status'], data['obs'], data['user_id'])
        return update_notebook(id ,update_notebook_dto)

    @app.route('/notebooks/<int:id>', methods=['DELETE'])
    def delete_notebook_route(id):
        return delete_notebook(id)