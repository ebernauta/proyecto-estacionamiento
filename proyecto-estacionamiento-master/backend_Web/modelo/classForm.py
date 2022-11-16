class FormularioAlumnos:
    def __init__(self,nombres="", rut="", telefono="", patente="", carrera="", horario=""):
        self.nombres = nombres
        self.rut = rut
        self.telefono = telefono
        self.patente = patente
        self.carrera = carrera
        self.horario = horario
    
    def __str__(self):
        return f'Nombre: {self.nombres}, Rut: {self.rut}, Telefono: {self.telefono}, Patente: {self.patente}, Carrera: {self.carrera}, Horario: {self.horario}'
    
    def agregarAlumnos(self):
        return{
            'nombres': self.nombres,
            'rut': self.rut,
            'telefono': self.telefono,
            'patente': self.patente,
            'carrera': self.carrera,
            'horarioClases': self.horario,
        }
    

class FormularioFuncionarios:
    def __init__(self, nombre="", rut="", telefono="", patente="", cargo=""):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono
        self.patente = patente
        self.cargo = cargo
        
        
    def __str__(self):
        return f'Nombre: {self.nombre}, Rut: {self.rut}, Telefono: {self.telefono}, Patente: {self.patente}, Cargo: {self.cargo}'
    
    def agregarFuncionarios(self):
        return{
            'nombre': self.nombre,
            'rut': self.rut,
            'numeroTelefonico': self.telefono,
            'patente': self.patente,
            'cargo': self.cargo,
        }