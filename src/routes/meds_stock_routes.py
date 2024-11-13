from controllers.meds_stock_controller import get_all_meds_stock
from controllers.meds_stock_controller import get_meds_stock_by_id
from controllers.meds_stock_controller import create_meds_stock
from controllers.meds_stock_controller import update_meds_stock
from controllers.meds_stock_controller import delete_meds_stock
from flask import request

#DTOS
from dtos.meds_stock.create_meds_stock_dto import MedsStockDTO
from dtos.meds_stock.update_meds_stock_dto import UpdateMedsStockDTO

def meds_stock(app):
    @app.route('/meds-stock', methods=['GET'])
    def get_all_meds_stock_route():
        return get_all_meds_stock()
    
    @app.route('/meds-stock/<int:id>', methods=['GET'])
    def get_meds_stock_by_id_route(id):
        return get_meds_stock_by_id(id)
    
    @app.route('/medstock', methods=['POST'])
    def create_meds_stock_route():
        data = request.get_json()
        create_meds_stock_dto = MedsStockDTO(data['med_name'], data['med_qtd'], data['med_val'], data['med_desc'], data['med_type'], data['user_id'])
        return create_meds_stock(create_meds_stock_dto)
    
    @app.route('/meds-stock/<int:id>', methods=['PUT'])
    def update_meds_stock_route(id):
        data = request.get_json()
        update_meds_stock_dto = UpdateMedsStockDTO(data['med_name'], data['med_qtd'], data['med_val'], data['med_desc'], data['med_type'], data['user_id'])
        return update_meds_stock(id, update_meds_stock_dto)
    
    @app.route('/meds-stock/<int:id>', methods=['DELETE'])
    def delete_meds_stock_route(id):
        return delete_meds_stock(id)