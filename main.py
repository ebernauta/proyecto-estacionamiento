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
        contrasena = request.form['contraseña']
        if user:
            if usuario == 'guardia' and contrasena:
                return render_template('mainGuardia.html')
            elif usuario == 'admin' and contrasena:
                return render_template('mainAdmin.html')
            return render_template('index.html')
        else:
            print('Usuario o contraseña incorrectos')
        
        return render_template('login.html' , form=form)
    else:
        return render_template('login.html' , form=form)


@app.route("/", methods=['GET', 'POST'])
def raiz():
    return redirect(url_for('login'))

@app.route("/main", methods=['GET', 'POST'])
def main():
    form = MyForm()
    estacionados = db['Estacionados']
    colEstacionados = list(estacionados.find({}))
    contadorEstacionados = len(colEstacionados)
    return render_template("main.html", form = form, estacionados = colEstacionados, contadorEstacionados = contadorEstacionados)

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

@app.route("/datosAlumnos", methods=['GET'])
def datosAlumnos():
    form = MyForm()
    alumnos = db['Alumnos']
    colAlumnos = list(alumnos.find({}))
    nuevaLista = []
    for i in colAlumnos:
        dic = {}
        dic["nombres"] = i["nombres"]
        dic["rut"] = i["rut"]
        dic["telefono"] = i["telefono"]
        dic["patente"] = i["patente"]
        dic["carrera"] = i["carrera"]
        dic["horarioClases"] = i["horarioClases"]
        dic["cargo"] = i["cargo"]
        nuevaLista.append(dic)
    return jsonify({"datosAlum": nuevaLista})

@app.route("/datosFuncionarios", methods=['GET'])
def datosFuncionarios():
    form = MyForm()
    funcionarios = db['Funcionarios']
    colFuncionarios = list(funcionarios.find({}))
    nuevaLista = []
    for i in colFuncionarios:
        dic = {}
        dic["nombres"] = i["nombres"]
        dic["rut"] = i["rut"]
        dic["telefono"] = i["telefono"]
        dic["patente"] = i["patente"]
        dic["carrera"] = i["carrera"]
        dic["horarioClases"] = i["horarioClases"]
        dic["cargo"] = i["cargo"]
        nuevaLista.append(dic)
    return jsonify({"datosFunc": nuevaLista})

    
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
            # qr
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

@app.route('/tablaDatos', methods=['GET', 'POST'])
def tablaDatos():
    form = MyForm()
    return render_template("tablaDatos.html", form = form)

@app.route('/scanEntrada', methods=["POST", "GET"])
def scanEntrada():
    form = MyForm()
    if request.method == "POST":
        patente = request.form['patente']
        colEstacionados = db['Estacionados']
        colAlumnos = db['Alumnos']
        colFuncionarios = db['Funcionarios']
        busquedaAlumno = colAlumnos.find_one({"patente": patente})
        busquedaFuncionario = colFuncionarios.find_one({"patente": patente})
        if busquedaAlumno:
            colEstacionados.insert_one(busquedaAlumno)
            
            return redirect(url_for('aprobado'))
        elif busquedaFuncionario:
            colEstacionados.insert_one(busquedaFuncionario)
            
            return redirect(url_for('aprobado'))
        else:
            return redirect(url_for('rechazado'))
    return render_template("scaneo.html", form = form)

@app.route('/scanSalida', methods=["POST", "GET"])
def scanSalida():
    form = MyForm()
    if request.method == "POST":
        patente = request.form['patente']
        colEstacionados = db['Estacionados']
        colAlumnos = db['Alumnos']
        colFuncionarios = db['Funcionarios']
        busquedaAlumno = colAlumnos.find_one({"patente": patente})
        busquedaFuncionario = colFuncionarios.find_one({"patente": patente})
        if busquedaAlumno:
            colEstacionados.delete_one(busquedaAlumno)
            
            return redirect(url_for('salida'))
        elif busquedaFuncionario:
            colEstacionados.delete_one(busquedaFuncionario)
            
            return redirect(url_for('salida'))
        else:
            return redirect(url_for('rechazado'))
    return render_template("scaneo.html", form = form)


# salida estacionamiento 
@app.route('/salida', methods=['GET', 'POST'])
def salida():
    form = MyForm()
    return render_template("salida.html", form = form)

@app.route('/aprobado', methods=["POST", "GET"])
def aprobado():
    form = MyForm()
    return render_template("aprobado.html", form = form)

@app.route('/rechazado', methods=["POST", "GET"])
def rechazado():
    form = MyForm()
    return render_template("rechazado.html", form = form)


if __name__ == '__main__':    
    app.run(debug=False)