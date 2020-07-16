from db import sql_connection

con = sql_connection()
class Profesores:
    def __init__(self, id, profesores, nombre, apellido, usuario, password, codigo):
        self.id = id
        self.profesores = profesores
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password
        self.codigo = codigo
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
