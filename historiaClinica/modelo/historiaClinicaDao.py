from sqlite3.dbapi2 import Cursor
from turtle import title
from .conexion import ConexionDB
from tkinter import messagebox

def listarHistoria(idPersona):
    conexion = ConexionDB()
    listaHistoria = []
    sql = f'SELECT h.idHistoriaClinica, p.nombre || " " || p.apellido AS NombreCompleto, h.fechaHistoria, h.motivoDeConsulta, h.tipoDeAlimentacion, h.actividadFisica, h.digestion, h.medicacion, h.operacionesCicatrices, h.embarazos, h.traumatismos, h.observaciones FROM historiaClinica h INNER JOIN Persona p ON p.idPersona = h.idPersona WHERE p.idPersona = {idPersona}'

    try:
        conexion.cursor.execute(sql)
        listaHistoria = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'LISTAR HISTORIA'
        mensaje = 'Error al listar historia medica'
        messagebox.showerror(title, mensaje)
    return listaHistoria

def guardarHistoria(idPersona, fechaHistoria, motivoDeConsulta, tipoDeAlimentacion, actividadFisica, digestion, medicacion, operacionesCicatrices, embarazos, traumatismos, observaciones):
    conexion = ConexionDB()
    sql = f"""INSERT INTO historiaClinica (idPersona, fechaHistoria, motivoDeConsulta, tipoDeAlimentacion, actividadFisica, digestion, medicacion, operacionesCicatrices, embarazos, traumatismos, observaciones) VALUES 
            ({idPersona}, '{fechaHistoria}', '{motivoDeConsulta}', '{tipoDeAlimentacion}', '{actividadFisica}', '{digestion}', '{medicacion}', '{operacionesCicatrices}', '{embarazos}', '{traumatismos}', '{observaciones}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registro Historia Clinica'
        mensaje = 'Historia registrada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registro Historia Clinica'
        mensaje = 'Error al registrar historia'
        messagebox.showerror(title, mensaje)

def eliminarHistoria(idHistoriaClinica):
    conexion = ConexionDB()
    sql = f'DELETE FROM historiaClinica WHERE idHistoriaClinica = {idHistoriaClinica}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Historia'
        mensaje = 'Historia Clinica eliminada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Historia'
        mensaje = 'Error al eliminar historia clinica'
        messagebox.showerror(title, mensaje)


class historiaClinica:
    def __init__(self, idPersona, fechaHistoria, motivoDeConsulta, tipoDeAlimentacion, actividadFisica, digestion, medicacion, operacionesCicatrices, embarazos, traumatismos, observaciones):
        self.idHistoriaClinica = None
        self.idPersona = idPersona
        self.fechaHistoria = fechaHistoria
        self.motivoDeConsulta = motivoDeConsulta
        self.tipoDeAlimentacion = tipoDeAlimentacion
        self.actividadFisica = actividadFisica 
        self.digestion = digestion
        self.medicacion = medicacion
        self.operacionesCicatrices = operacionesCicatrices
        self.embarazos = embarazos
        self.traumatismos = traumatismos
        self.observaciones = observaciones

    def __str__(self):
        return f'historiaClinica[{self.idPersona}, {self.fechaHistoria}, {self.motivoDeConsulta}, {self.tipoDeAlimentacion}, {self.actividadFisica}, {self.digestion}, {self.medicacion}, {self.operacionesCicatrices}, {self.embarazos}, {self.traumatismos}, {self.observaciones}]'
        
    