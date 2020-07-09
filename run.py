# Del modulo app importamos la funcion create_app
from app import create_app
 
app = create_app('default')
app.run()

