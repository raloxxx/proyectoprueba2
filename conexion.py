

# connect = sql_connection()

# # cursorObj = connect.cursor()
# # cursorObj.execute("""
# #         CREATE TABLE prueba(
# #             id integer PRIMARY KEY,
# #             name text
# #         )
# #     """)

# cursorObj = connect.cursor()
# cursorObj.execute("""
#         INSERT INTO prueba(id, name)
#         VALUES(2, 'Jose')
#     """)
# connect.commit()
# cursorObj.execute("""
#         SELECT * FROM prueba
#     """)
# rows = cursorObj.fetchall()

# for row in rows:
#     print(row)
