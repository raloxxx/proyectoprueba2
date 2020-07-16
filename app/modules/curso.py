# Una clase esta definida por atributos y metodos
# atributos = variables
# metodos = funciones

#        Curso

# instancias
# Matematica       Comunicacion      Religion

class Curso:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
