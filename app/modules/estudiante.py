from db import sql_connection

con = sql_connection()
class Estudiante:
    def __init__(self, id, estudiantes, nombre, apellido, usuario, password, codigo):
        self.id = id
        self.estudiantes = estudiantes
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password
        self.codigo = codigo
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id