from db import sql_connection

con = sql_connection()
class Nota:
    def __init__(self, id, unidad, nota, id_actividad):
        self.id = id
        self.unidad = unidad
        self.nota = nota
        self.id_actividad = id_actividad

    def guardarNota(self):
        cursor = con.cursor()
        cursor.execute("INSERT INTO nota(id, unidad, nota, id_actividad) VALUES(" + str(self.id) + "," + str(self.unidad) + "," + str(self.nota) + ',' + str(self.id_actividad) + ";")
        con.commit()
        con.close()

    
    def listarNotas(self):
        cursor = con.cursor()
        cursor.execute("""
            SELECT * FROM prueba
        """)
        rows = cursor.fetchall()
        return rows