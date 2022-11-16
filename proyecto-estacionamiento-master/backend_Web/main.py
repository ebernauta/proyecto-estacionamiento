from flask import Flask, jsonify, render_template, redirect, url_for, request, flash
from flask_wtf import CSRFProtect, FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import modelo.classForm as classForm
import dao.database as database
from pymongo import MongoClient

db = database.conexion()

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

csrf = CSRFProtect(app)

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    patente = StringField('name', validators=[DataRequired()])

@app.route('/')
def login():
    if request.method == 'POST':
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')



@app.route("/main")
def main():    
    return render_template("main.html")


@app.route('/registrarAlumno', methods=['GET', 'POST'])
def registar_alumno():
    form = MyForm()
    if request.method == 'POST':
        colAlumnos = db['Alumnos']
        nombres = request.form['nombres']
        patente = request.form['patente']
        rut = request.form['rut']
        telefono = request.form['telefono']
        carrera = request.form['carrera']
        horario = request.form['horario']
        if(nombres == ''):
            flash("Ingrese su Nombre", "danger")
            return redirect(url_for('registar_alumno'))
        elif (patente == ''):
            flash("Ingrese su Patente", "danger")
            return redirect(url_for('registar_alumno'))
        elif (rut == ''):
            flash("Ingrese su Rut", "danger")
            return redirect(url_for('registar_alumno'))
        elif (telefono == ''):
            flash("Ingrese su Numero", "danger")
            return redirect(url_for('registar_alumno'))
        elif (carrera == ''):
            flash("Ingrese su Carrera", "danger")
            return redirect(url_for('registar_alumno'))
        elif (horario == ''):
            flash("Ingrese su Carrera", "danger")
            return redirect(url_for('registar_alumno'))
        alumnos = classForm.FormularioAlumnos(nombres, rut, telefono, patente, carrera, horario)
        colAlumnos.insert_one(alumnos.agregarAlumnos())    
        flash("Alumno registrado con exito", "success")
        return redirect(url_for('registar_alumno'))
    else:        
        return render_template("registrarAlumno.html", form = form)    

@app.route("/alumnoRegistrado",  methods=["POST", "GET"])
def alumnoRegistrado():
    
    return render_template("alumnoRegistrado.html")


@app.route('/registrarFuncionario', methods=['GET', 'POST'])
def registrar_funcionario():
    form = MyForm()
    if request.method == 'POST':
        colFuncionarios = db['Funcionarios']
        
        nombre = request.form['nombre']
        rut = request.form['rut']
        numeroTelefonico = request.form['numeroTelefonico']
        patente = request.form['patente']
        cargo = request.form['cargo']
        
        if (nombre == ''):
            flash("Ingrese su Nombre", "danger")
            return redirect(url_for('registrar_funcionario'))
        elif (rut == ''):
            flash("Ingrese su Rut", "danger")
            return redirect(url_for('registrar_funcionario'))
        elif (numeroTelefonico == ''):
            flash("Ingrese su numeroTelefonico", "danger")
            return redirect(url_for('registrar_funcionario'))
        elif (patente == ''):
            flash("Ingrese su Patente", "danger")
            return redirect(url_for('registrar_funcionario'))
        elif (cargo == ''):
            flash("Ingrese su Cargo", "danger")
            return redirect(url_for('registrar_funcionario'))
        
        funcionarios = classForm.FormularioFuncionarios(nombre, rut, numeroTelefonico, patente, cargo)
        colFuncionarios.insert_one(funcionarios.agregarFuncionarios())
        flash("Registro exitoso", "success")
        return redirect(url_for('registrar_funcionario'))
    else:
        return render_template("registrarFuncionario.html", form = form)

@app.route('/funcionarioRegistrado', methods=["POST", 'GET'])
def funcionarioRegistrado():
    
    return render_template("registrarFuncionario.html")

@app.route('/charts', methods=["POST", "GET"])
def charts():
    
    return render_template("charts.html")

@app.route('/tables', methods=["POST", "GET"])
def tables():
    
    return render_template("tables.html")




@app.route('/scan', methods=["POST", "GET"])
def scan():
    form = MyForm()
    if request.method == "POST":
        dato = request.form['dato']
        return f"El dato es: {dato}"
    
    return render_template("scan2.html", form = form)
    

if __name__ == '__main__':    
    app.run(debug=True)