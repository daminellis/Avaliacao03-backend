from flask import jsonify
from flask_jwt_extended import create_access_token
from datetime import timedelta

#MODEL
from models.user_model import User

#DTO
from dtos.login.login_dto import LoginDTO
from dtos.responses.success.login_success_dto import LoginSuccessDTO
from dtos.responses.error.error_dto import ErrorDTO

def authentication(login_dto: LoginDTO):
    user = User.query.filter_by(first_name=login_dto.first_name).first()

    if user and user.password == login_dto.password:
        token =create_access_token(identity=user.to_dict(), expires_delta=timedelta(days=1))
        
        return jsonify(LoginSuccessDTO(code=200, access_token=token)), 200
    else:
        return jsonify(ErrorDTO(code= 401, message="Nome de usuário ou senha incorretos!", details= ['path: POST auth/login'])), 401
