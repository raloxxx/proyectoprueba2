# Importar el motor de plantillas
from flask import render_template

# Importamos el modulo
from app.modules import nota

# Creamos una funcion llamada estudiante_router(app)
def estudiante_router(app):

    #Definimos la ruta
    @app.route('/')
    def listar():
        return render_template('estudiante.html', estudiantes = {
            'nombre': 'Juan Manuel',
            'apellido': 'Delgado Marcos'
        })
    @app.route('/guardar')
    def guardar():
        nota1 = nota.Nota(1, 2, 12, 1)
        nota1.guardarNota()
        return "Vengo de cambio"

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