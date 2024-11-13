from auth.auth_service import authentication
from flask import request

#DTO
from dtos.login.login_dto import LoginDTO

def login(app):
    @app.route('/auth/login', methods=['POST'])
    def login_route():
        data = request.get_json()
        login_dto = LoginDTO(data['first_name'], data['password'])
        return authentication(login_dto)
