# Importar el motor de plantillas
from flask import render_template, request #JINJA



# Creamos una funcion llamada estudiante_router(app)
def estudiante_router(app, db):

    #http://www.localhost:5000/
    #Definimos la ruta
    @app.route('/')
    def listar():
        conn = db.connect() # Conexión a la Base de Datos
        query = conn.execute("select * from estudiante")  # Esta línea ejecuta un query y retorna un json como resultado
        estudiantes = {'estudiantes': [i[0] for i in query.cursor.fetchall()]}

        return render_template('estudiante.html', estudiantes=estudiantes)

    @app.route('/guardar', methods=['POST'])
    def guardar():
        nombre = request.form['nombres']
        apellido = request.form['apellido']
        # INSERT INTO estudiante() value ()
        return nombre + apellido

    @app.route('/listar')
    def listar2():
        nota = nota.Nota(2, 2, 12, 1)
        return nota.listarNotas()

    @app.route('/editar')
    def editar():
        return 'views/alumno.html'

    @app.route('/borrar')
    def borrar():
        return 'views/alumno.html'