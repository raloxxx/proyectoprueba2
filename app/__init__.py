# importamos la libreria flask
from flask import Flask
from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# importamos la configuracion
from config import config

from app.router import estudiante, profesor, curso


def create_app(config_name):
    # Configuramos el entorno de flask
    db_connect = create_engine('sqlite:///app/proyectoICC.db')
    # Session = sessionmaker(bind=db_connect)
    # session = Session()

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # -------------------------
    #profesor.profesor_routes(app)
    estudiante.estudiante_router(app, db_connect)
    curso.curso_router(app, db_connect)
 
    return app