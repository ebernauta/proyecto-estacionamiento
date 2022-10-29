from django.shortcuts import render
from flask import Flask, jsonify, render_template, redirect, url_for, request, flash
from flask_wtf import CSRFProtect
import modelo.classForm as classForm
import dao.database as database
from pymongo import MongoClient

db = database.conexion()

app = Flask(__name__)
csrf = CSRFProtect(app)

@app.route("/main")
def main():
    
    return render_template("main.html")

@app.route("/registrarAlumno", methods=["GET", "POST"])
def alumno():
    
    return render_template("registrarAlumno.html")

@app.route('/alumnoRegistrado', methods=['GET', 'POST'])
def registar_alumno():
    if request.method == 'POST':
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
        
        flash("Alumno registrado con exito", "success")
    return render_template("registrarAlumno.html")

@app.route("/alumnoRegistrado",  methods=["POST", "GET"])
def alumnoRegistrado():
    
    return render_template("alumnoRegistrado.html")


@app.route("/registrarFuncionario", methods=["POST", "GET"])
def registrar_funcionario():
    
    return render_template("registrarFuncionario.html")


@app.route('/funcionarioRegistrado', methods=['GET', 'POST'])
def funcionarioRegistrado():
    if request == 'POST':
        colFuncionarios = db['Funcionarios']
        nombre = request.form['nombre']
        print(nombre)
        rut = request.form['rut']
        numeroTelefonico = request.form['numeroTelefonico']
        patente = request.form['patente']
        cargo = request.form['cargo']
        
        funcionarios = classForm.FormularioFuncionarios(nombre, rut, numeroTelefonico, patente, cargo)
        colFuncionarios.insert_one(funcionarios.agregarFuncionarios())
        response = jsonify({
            'nombre': nombre,
            'rut': rut,
            'numeroTelefonico': numeroTelefonico,
            'patente': patente,
            'cargo': cargo, 
        })
        flash("Registro exitoso", "success")
    return render_template("registrarFuncionario.html")


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
