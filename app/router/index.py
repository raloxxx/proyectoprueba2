# Importar el motor de plantillas
from flask import render_template, request #JINJA



# Creamos una funcion llamada estudiante_router(app)
def index_router(app, db):

    #http://www.localhost:5000/
    #Definimos la ruta
    @app.route('/')
    def index():

        return render_template('index.html')

    