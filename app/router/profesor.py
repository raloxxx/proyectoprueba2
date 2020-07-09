from flask import render_template

def profesor_routes(app):

    @app.route('/profesor/listar')
    def listar_profesores():
        """
            Aqui pongo mi codigo fuente
        """
        suma = 0
        a = 7
        b = 8

        suma = a + b
        return str(suma)

    @app.route('/profesor/guardar')
    def guardar_profesores():
        return "guardar profesores"