# importamos la libreria flask
from flask import Flask

# importamos la configuracion
from config import config


#
from app.router import estudiante, profesor


def create_app(config_name):
    # Configuramos el entorno de flask
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # -------------------------
    profesor.profesor_routes(app)
    estudiante.estudiante_router(app)
 
    return app