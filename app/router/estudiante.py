from flask import render_template


def estudiante_router(app):

    @app.route('/')
    def listar():
        return render_template('estudiante.html', estudiantes = {
            'nombre': 'Juan Manuel',
            'apellido': 'Delgado Marcos'
        })

    @app.route('/guardar')
    def guardar():
        return 'views/profesor.html'

    @app.route('/editar')
    def editar():
        return 'views/alumno.html'

    @app.route('/borrar')
    def borrar():
        return 'views/alumno.html'