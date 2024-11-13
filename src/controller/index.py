#  Criação das rotas de acesso a aplicação
#  from routes.nomedarota import nome da definicao


# Importando as rotas
from controller.user_controller import users
from controller.notebook_controller import notebook
from controller.meds_stock_controller import meds_stock
from controller.login_controller import login

def default_routes(app):
    #nomde da definicao
    users(app)
    notebook(app)
    meds_stock(app)
    login(app)