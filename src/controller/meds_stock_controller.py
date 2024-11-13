from service.meds_stock_service import get_all_meds_stock
from service.meds_stock_service import get_meds_stock_by_id
from service.meds_stock_service import create_meds_stock
from service.meds_stock_service import update_meds_stock
from service.meds_stock_service import delete_meds_stock

from flask import request
from flask_jwt_extended import jwt_required

#Repository
from repository.meds_stock.create_meds_stock_repository import MedsStockRepository
from repository.meds_stock.update_meds_stock_repository import UpdateMedsStockRepository

def meds_stock(app):
    @app.route('/meds-stock', methods=['GET'])
    @jwt_required()
    def get_all_meds_stock_route():
        return get_all_meds_stock()
    
    @app.route('/meds-stock/<int:id>', methods=['GET'])
    @jwt_required()
    def get_meds_stock_by_id_route(id):
        return get_meds_stock_by_id(id)
    
    @app.route('/medstock', methods=['POST'])
    @jwt_required()
    def create_meds_stock_route():
        data = request.get_json()
        create_meds_stock_rep = MedsStockRepository(data['med_name'], data['med_qtd'], data['med_val'], data['med_desc'], data['med_type'], data['user_id'])
        return create_meds_stock(create_meds_stock_rep)
    
    @app.route('/meds-stock/<int:id>', methods=['PATCH'])
    @jwt_required()
    def update_meds_stock_route(id):
        data = request.get_json()
        update_meds_stock_rep = UpdateMedsStockRepository(data['med_name'], data['med_qtd'], data['med_val'], data['med_desc'], data['med_type'], data['user_id'])
        return update_meds_stock(id, update_meds_stock_rep)
    
    @app.route('/meds-stock/<int:id>', methods=['DELETE'])
    @jwt_required()
    def delete_meds_stock_route(id):
        return delete_meds_stock(id)