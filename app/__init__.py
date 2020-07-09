from flask import Flask
from config import config

from app.router import estudiante
 
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    estudiante.estudiante_router(app)
 
    return app