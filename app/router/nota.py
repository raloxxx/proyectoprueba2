# Importar el motor de plantillas
from flask import render_template, request #JINJA



# Creamos una funcion llamada estudiante_router(app)
def nota_router(app, db):

    #http://www.localhost:5000/
    #Definimos la ruta
    @app.route('/nota')
    def listar_notas():
        conn = db.connect() # Conexión a la Base de Datos
        query = conn.execute("select * from nota")  # Esta línea ejecuta un query y retorna un json como resultado
        notas = {'notas': [i[0] for i in query.cursor.fetchall()]}

        return render_template('nota.html', notas=notas)

    