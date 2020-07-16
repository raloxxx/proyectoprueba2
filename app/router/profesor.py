# Importar el motor de plantillas
from flask import render_template, request #JINJA



# Creamos una funcion llamada estudiante_router(app)
def profesor_router(app, db):

    #http://www.localhost:5000/
    #Definimos la ruta
    @app.route('/profesor')
    def listar_profesor():
        conn = db.connect() # Conexión a la Base de Datos
        query = conn.execute("select * from profesor")  # Esta línea ejecuta un query y retorna un json como resultado
        profesors = {'profesors': [i[0] for i in query.cursor.fetchall()]}

        return render_template('profesor.html', profesors=profesors)

    