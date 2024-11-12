from controllers.meds_stock_controller import get_all_meds_stock
from controllers.meds_stock_controller import get_meds_stock_by_id
from controllers.meds_stock_controller import create_meds_stock
from controllers.meds_stock_controller import update_meds_stock
from controllers.meds_stock_controller import delete_meds_stock
from flask import request

def meds_stock(app):
    app.route('/getallmedsstock', methods=['GET'])(get_all_meds_stock)
    app.route('/getmedsstockbyid/<int:meds_stock_id>', methods=['GET'])(get_meds_stock_by_id)
    app.route('/createmedsstock', methods=['POST'])(create_meds_stock)
    app.route('/updatemedsstock/<int:meds_stock_id>', methods=['PUT'])(update_meds_stock)
    app.route('/deletemedsstock/<int:meds_stock_id>', methods=['DELETE'])(delete_meds_stock)