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
    
    @app.route('/meds-stock/<int:meds_stock_id>', methods=['GET'])
    def get_meds_stock_by_id_route(meds_stock_id):
        return get_meds_stock_by_id(meds_stock_id)
    
    @app.route('/medstock', methods=['POST'])
    def create_meds_stock_route():
        data = request.get_json()
        meds_stock_dto = MedsStockDTO(data['meds_name'], data['meds_qtd'], data['meds_val'], data['mds_desc'], data['meds_type'], data['person_id'])
        return create_meds_stock(meds_stock_dto)
    
    @app.route('/meds-stock/<int:meds_stock_id>', methods=['PUT'])
    def update_meds_stock_route(meds_stock_id):
        data = request.get_json()
        update_meds_stock_dto = UpdateMedsStockDTO(data['meds_name'], data['meds_qtd'], data['meds_val'], data['mds_desc'], data['meds_type'], data['person_id'])
        return update_meds_stock(meds_stock_id, update_meds_stock_dto)
    
    @app.route('/meds-stock/<int:meds_stock_id>', methods=['DELETE'])
    def delete_meds_stock_route(meds_stock_id):
        return delete_meds_stock(meds_stock_id)