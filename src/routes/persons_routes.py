from controllers.persons_controller import get_all_persons

def persons(app):
    app.route('/getpersons', methods=['GET'])(get_all_persons)
