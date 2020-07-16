
class Nota:
    def __init__(self, id, unidad, nota, id_actividad):
        self.id = id
        self.unidad = unidad
        self.nota = nota
        self.id_actividad = id_actividad

    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id