from .conexion import ConexionDB
from tkinter import messagebox


def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona (nombre, apellido, dni, fechaNacimiento, edad, 
            antecedentes, hijos, ocupacion, telefono, correo, activo) VALUES
            ('{persona.nombre}', '{persona.apellido}', {persona.dni}, '{persona.fechaNacimiento}',
            {persona.edad}, '{persona.antecedentes}', '{persona.hijos}', '{persona.ocupacion}', 
            '{persona.telefono}','{persona.correo}',1)"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Paciente'
        mensaje = 'Paciente Registrado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registrar Paciente'
        mensaje = 'Error al registrar paciente'
        messagebox.showerror(title,mensaje)

def listar():
    conexion = ConexionDB()

    listaPersona = []
    sql = 'SELECT * FROM Persona WHERE activo = 1'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(title,mensaje)
    return listaPersona

def listarCondicion(where):
    conexion = ConexionDB()
    listaPersona = []
    sql = f'SELECT * FROM Persona {where}'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(title,mensaje)
    return listaPersona

def eliminarPaciente(idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Paciente'
        mensaje = 'Paciente eliminado exitosamente'
        messagebox.showwarning(title,mensaje)
    except:
        title = 'Eliminar Paciente'
        mensaje = 'Error al eliminar Paciente'
        messagebox.showwarning(title,mensaje)





class Persona:
    def __init__(self, nombre, apellido, dni, fechaNacimiento, edad, antecedentes, hijos, ocupacion, telefono, correo):
        self.idPersona = None
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fechaNacimiento = fechaNacimiento
        self.edad = edad
        self.antecedentes = antecedentes
        self.hijos = hijos
        self.ocupacion = ocupacion
        self.telefono = telefono
        self.correo = correo

    def __srt__(self):
        return f'Persona[{self.nombre}, {self.apellido}, {self.dni}, {self.fechaNacimiento}, {self.edad}, {self.antecedentes}, {self.hijos}, {self.ocupacion}, {self.telefono}, {self.correo}]'