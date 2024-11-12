from controllers.notebook_controller import get_all_notebooks
from controllers.notebook_controller import get_notebook_by_id
from controllers.notebook_controller import create_notebook
from controllers.notebook_controller import update_notebook
from controllers.notebook_controller import delete_notebook
from flask import request

def notebook(app):
    app.route('/getallnotebooks', methods=['GET'])(get_all_notebooks)
    app.route('/getnotebookbyid/<int:notebook_id>', methods=['GET'])(get_notebook_by_id)
    app.route('/createnotebook', methods=['POST'])(create_notebook)
    app.route('/updatenotebook/<int:id>', methods=['PUT'])(update_notebook)
    app.route('/deletenotebook/<int:notebook_id>', methods=['DELETE'])(delete_notebook)