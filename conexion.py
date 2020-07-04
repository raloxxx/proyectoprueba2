import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('prueba.db')

        return con

    except Error:

        print(Error)


connect = sql_connection()

# cursorObj = connect.cursor()
# cursorObj.execute("""
#         CREATE TABLE prueba(
#             id integer PRIMARY KEY,
#             name text
#         )
#     """)

cursorObj = connect.cursor()
cursorObj.execute("""
        INSERT INTO prueba(id, name)
        VALUES(2, 'Jose')
    """)
connect.commit()
cursorObj.execute("""
        SELECT * FROM prueba
    """)
rows = cursorObj.fetchall()

for row in rows:
    print(row)


class Curso:

    id = ''
    nombre = ''
    profesor_asignado = ''

    #constructor
    def __init__(self, id, nombre, profesor_asignado):
        self.id = id
        self.nombre = nombre
        self.profesor_asignado = profesor_asignado

    def listarCursos(self):
        connect = sql_connection()
        cursorObj = connect.cursor()
        cursorObj.execute("""
            SELECT * FROM prueba
        """)
        rows = cursorObj.fetchall()
        return rows
    # def crear(self):

    # def borrar(self):

    # def editar(self):

curso = Curso('1', "matematica", "raul")