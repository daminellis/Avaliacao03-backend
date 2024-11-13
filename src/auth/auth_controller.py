from flask import jsonify
from flask_jwt_extended import create_access_token
from datetime import timedelta

#MODEL
from models.user_model import Log

#DTO
from dtos.login.login_dto import LoginDTO

def authentication(login_dto: LoginDTO):
    user = Log.query.filter_by(first_name=login_dto.first_name).first()

    if user and user.password == login_dto.password:
        access_token =create_access_token(identity=user.to_dict(), expires_delta=timedelta(days=1))
        return jsonify({
            "success": True,
            "access_token": access_token
        }), 200
    else:
        return jsonify({
            "success": False,
            "error": "Usuário ou senha incorretos"
        }), 401