#  Criação das rotas de acesso a aplicação
#  from routes.nomedarota import nome da definicao

from routes.persons_routes import persons
from routes.notebook_routes import notebook
from routes.meds_stock_routes import meds_stock 

def default_routes(app):
    #nomde da definicao
    persons(app)
    notebook(app)
    meds_stock(app)