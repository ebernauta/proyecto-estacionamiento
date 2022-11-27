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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if request.method == 'POST':
        Login = db['Login']
        user = Login.find_one({'usuario' : request.form['usuario']}, {'contraseña' : request.form['contraseña']})
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        if user:
            if usuario == 'guardia' and contraseña:
                return render_template('mainGuardia.html')
            elif usuario == 'admin' and contraseña:
                return render_template('mainAdmin.html')
            return render_template('index.html')
        else:
            print('Usuario o contraseña incorrectos')
        
        return render_template('login.html' , form=form)
    else:
        return render_template('login.html' , form=form)

@app.route("/base")
def base():
    return render_template('base.html')

@app.route("/index01")
def index01():
    return render_template('index01.html')

@app.route("/main", methods=['GET', 'POST'])
def main():
    form = MyForm()
    estacionados = db['Estacionados']
    colEstacionados = list(estacionados.find({}))
    contadorEstacionados = len(colEstacionados)
    print(contadorEstacionados)
    return render_template("mainPrueba.html", form = form, estacionados = colEstacionados, contadorEstacionados = contadorEstacionados)

@app.route("/datos", methods=['GET'])
def datos():
    form = MyForm()
    estacionados = db['Estacionados']
    colEstacionados = list(estacionados.find({}))
    contadorEstacionados = len(colEstacionados)
    nuevaLista = []
    for i in colEstacionados:
        dic = {}
        dic["nombres"] = i["nombres"]
        dic["rut"] = i["rut"]
        dic["telefono"] = i["telefono"]
        dic["patente"] = i["patente"]
        dic["carrera"] = i["carrera"]
        dic["horarioClases"] = i["horarioClases"]
        dic["cargo"] = i["cargo"]
        nuevaLista.append(dic)
    return jsonify({"datos": nuevaLista})
    
# @app.route("/main", methods=['GET', 'POST'])
# def main():
#     form = MyForm()
#     estacionados = db['Estacionados']
#     colEstacionados = list(estacionados.find({}))
#     contadorEstacionados = len(colEstacionados)
#     return render_template("main.html", form = form, estacionados = colEstacionados, contadorEstacionados = contadorEstacionados)



@app.route("/basti_test01")
def basti_test01():
    return render_template("escaner-basti.html")


@app.route('/registrarAlumno', methods=['GET', 'POST'])
def registrar_alumno():
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
            return redirect(url_for('registrar_alumno'))
        elif (patente == ''):
            flash("Ingrese su Patente", "danger")
            return redirect(url_for('registrar_alumno'))
        elif (rut == ''):
            flash("Ingrese su Rut", "danger")
            return redirect(url_for('registrar_alumno'))
        elif (telefono == ''):
            flash("Ingrese su Numero", "danger")
            return redirect(url_for('registrar_alumno'))
        elif (carrera == ''):
            flash("Ingrese su Carrera", "danger")
            return redirect(url_for('registrar_alumno'))
        elif (horario == ''):
            flash("Ingrese su Carrera", "danger")
            return redirect(url_for('registrar_alumno'))
        alumnos = classForm.FormularioAlumnos(nombres, rut, telefono, patente, carrera, horario)
        colAlumnos.insert_one(alumnos.agregarAlumnos())    
        flash("Alumno registrado con exito", "success")
        return redirect(url_for('registrar_alumno'))
    else:        
        return render_template("registrarAlumno.html", form = form)    

@app.route('/registrarFuncionario', methods=['GET', 'POST'])
def registrar_funcionario():
    form = MyForm()
    if request.method == 'POST':
        colFuncionarios = db['Funcionarios']
        nombre = request.form['nombres']
        rut = request.form['rut']
        numeroTelefonico = request.form['telefono']
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