# Importar el motor de plantillas
from flask import render_template, request #JINJA

from app.modules import curso

# Creamos una funcion llamada estudiante_router(app)
def curso_router(app, db):

    #http://www.localhost:5000/
    #Definimos la ruta
    @app.route('/curso')
    def cursolistar():
        conn = db.connect() # Conexión a la Base de Datos
        query = conn.execute("select * from curso")  # Esta línea ejecuta un query y retorna un json como resultado
        cursos = {'cursos': query.cursor.fetchall()}

        return render_template('curso.html', cursos=cursos)

    @app.route('/curso/guardar', methods=['POST'])
    def cursoguardar():
        conn = db.connect()

        id = request.form['id']
        nombre = request.form['nombre']
        cursoObj = curso.Curso(id, nombre)
        query = conn.execute("INSERT INTO curso(id, nombre) VALUES (?, ?)", 
        cursoObj.getId(), cursoObj.getNombre())

        query = conn.execute("select * from curso")  # Esta línea ejecuta un query y retorna un json como resultado
        cursos = {'cursos': query.cursor.fetchall()}

        return render_template('curso.html', cursos=cursos)
