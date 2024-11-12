#  Criação das rotas de acesso a aplicação
#  from routes.nomedarota import nome da definicao

from routes.user_routes import users
from routes.notebook_routes import notebook
from routes.meds_stock_routes import meds_stock 

def default_routes(app):
    #nomde da definicao
    users(app)
    notebook(app)
    meds_stock(app)