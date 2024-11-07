#  Criação das rotas de acesso a aplicação
#  from routes.nomedarota import nome da definicao

from routes.persons_routes import persons

def default_routes(app):
    #nomde da definicao
    persons(app)
