from flask import Flask
from flask_cors import CORS
from database.db import db
from routes.index import default_routes
from dotenv import load_dotenv
import os

class App:
    def __init__(self):
        load_dotenv()
        self.app = Flask(__name__)
        CORS(self.app)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}" #Mudar no .env de acordo com suas credenciais
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(self.app)
        default_routes(self.app)

    def run(self):
        self.app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    app = App()
    app.run() 