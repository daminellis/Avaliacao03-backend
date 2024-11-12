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
    
    @app.route('/notebooks/<int:notebook_id>', methods=['GET'])
    def get_notebook_by_id_route(notebook_id):
        return get_notebook_by_id(notebook_id)
    
    @app.route('/notebook', methods=['POST'])
    def create_notebook_route():
        data= request.get_json()
        notebook_dto= NotebookDTO(data['title'], data['med_name'], data['description'], data['method'], data['med_type'], data['med_freq'], data['qtd_taken'], data['qtd_total'], data['init_schedule'], data['end_schedule'], data['status'], data['obs'], data['person_id'] )
        return create_notebook(notebook_dto)

    @app.route('/notebooks/<int:notebook_id>', methods=['PUT'])
    def update_notebook_route(notebook_id):
        data= request.get_json()
        update_notebook_dto= UpdateNotebookDTO(data['title'], data['med_name'], data['description'], data['method'], data['med_type'], data['med_freq'], data['qtd_taken'], data['qtd_total'], data['init_schedule'], data['end_schedule'], data['status'], data['obs'], data['person_id'])
        return update_notebook(notebook_id ,update_notebook_dto)

    @app.route('/notebooks/<int:notebook_id>', methods=['DELETE'])
    def delete_notebook_route(notebook_id):
        return delete_notebook(notebook_id)