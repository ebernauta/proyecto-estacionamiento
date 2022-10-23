from flask import Flask, jsonify, render_template, redirect, url_for, request
import modelo.classForm as classForm
import dao.database as database
from pymongo import MongoClient

db = database.conexion()

app = Flask(__name__)

@app.route("/")
def main():
    
    return render_template("main.html")

@app.route("/registrarAlumno")
def alumno():
    
    return render_template("registrarAlumno.html")

@app.route('/alumnoRegistrado', methods=['GET', 'POST'])
def registar_alumno():
    colAlumnos = db['Alumnos']
    nombres = request.form['nombres']
    rut = request.form['rut']
    telefono = request.form['telefono']
    patente = request.form['patente']
    carrera = request.form['carrera']
    horario = request.form['horario']
    
    alumnos = classForm.FormularioAlumnos(nombres, rut, telefono, patente, carrera, horario)
    colAlumnos.insert_one(alumnos.agregarAlumnos())
    response = jsonify({
        'nombres': nombres,
        'rut': rut,
        'telefono': telefono,
        'patente': patente,
        'carrera': carrera,
        'horarioClases': horario
        
    })
    
    return f'Alumno registrado: {nombres}, {rut}, {telefono}, {patente}, {carrera}, {horario}'

# @app.route("/alumnoRegistrado",  methods=["POST", "GET"])
# def alumnoRegistrado():
    
#     return render_template("alumnoRegistrado.html")


app.run(debug= True)