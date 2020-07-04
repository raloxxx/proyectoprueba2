from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/profesor')
def profesor():
    return 'views/profesor.html'

@app.route('/alumno')
def alumno():
    return 'views/alumno.html'