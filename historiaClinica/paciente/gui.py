# INTERGAZ GRAFICA
from calendar import month
import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel, LabelFrame
from tkinter import messagebox
from turtle import title
from modelo.pacienteDao import Persona, guardarDatoPaciente, listarCondicion, listar, editarDatoPaciente, eliminarPaciente
from modelo.historiaClinicaDao import historiaClinica, guardarHistoria, listarHistoria, eliminarHistoria, editarHistoria
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date
class Frame(tk.Frame):
    def __init__(self,root):
        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#407e5e')  #7bbe9b
        self.idPersona = None
        self.idPersonaHistoria = None
        self.idHistoriaClinica = None
        self.idHistoriaClinicaEditar = None
        self.camposPaciente()
        self.deshabilitar()
        self.tablaPaciente()

    def camposPaciente(self):
        self.lblNombre = tk.Label(self,text='Nombre: ')
        self.lblNombre.config(font=('ARIAL',15,'bold'),bg='#407e5e',fg='#ffffff')
        self.lblNombre.grid(column=0, row=0,padx=10,pady=5)

        self.lblApellido = tk.Label(self,text='Apellido: ')
        self.lblApellido.config(font=('ARIAL',15,'bold'),bg='#407e5e',fg='#ffffff')
        self.lblApellido.grid(column=0, row=1,padx=10,pady=5)

        self.lblDni = tk.Label(self,text='DNI: ')
        self.lblDni.config(font=('ARIAL',15,'bold'),bg='#407e5e',fg='#ffffff')
        self.lblDni.grid(column=0, row=2,padx=10,pady=5)
        
        self.lblFechaNacimiento = tk.Label(self,text='Fecha de Nacimiento: ')
        self.lblFechaNacimiento.config(font=('ARIAL',15,'bold'),bg='#407e5e',fg='#ffffff')
        self.lblFechaNacimiento.grid(column=0, row=3,padx=10,pady=5)

        self.lblEdad = tk.Label(self,text='Edad: ')
        self.lblEdad.config(font=('ARIAL',15,'bold'),bg='#407e5e',fg='#ffffff')
        self.lblEdad.grid(column=0, row=4,padx=10,pady=5)

        self.lblAntecedentes = tk.Label(self,text='Antecedentes: ')
        self.lblAntecedentes.config(font=('ARIAL',15,'bold'),bg='#407e5e',fg='#ffffff')
        self.lblAntecedentes.grid(column=0, row=5,padx=10,pady=5)

        self.lblHijos = tk.Label(self,text='Hijos: ')
        self.lblHijos.config(font=('ARIAL',15,'bold'),bg='#407e5e',fg='#ffffff')
        self.lblHijos.grid(column=0, row=6,padx=10,pady=5)

        self.lblOcupacion = tk.Label(self,text='Ocupacion: ')
        self.lblOcupacion.config(font=('ARIAL',15,'bold'),bg='#407e5e',fg='#ffffff')
        self.lblOcupacion.grid(column=0, row=7,padx=10,pady=5)

        self.lblTelefono = tk.Label(self,text='Telefono: ')
        self.lblTelefono.config(font=('ARIAL',15,'bold'),bg='#407e5e',fg='#ffffff')
        self.lblTelefono.grid(column=0, row=8,padx=10,pady=5)

        self.lblCorreo = tk.Label(self,text='Correo: ')
        self.lblCorreo.config(font=('ARIAL',15,'bold'),bg='#407e5e',fg='#ffffff')
        self.lblCorreo.grid(column=0, row=9,padx=10,pady=5)

        #ENTRYS
        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=50,font=('ARIAL',15))
        self.entryNombre.grid(column=1,row=0, padx=10, pady=5, columnspan=2)

        self.svApellido = tk.StringVar()
        self.entryApellido = tk.Entry(self, textvariable=self.svApellido)
        self.entryApellido.config(width=50,font=('ARIAL',15))
        self.entryApellido.grid(column=1,row=1, padx=10, pady=5, columnspan=2)

        self.svDni = tk.StringVar()
        self.entryDni = tk.Entry(self, textvariable=self.svDni)
        self.entryDni.config(width=50,font=('ARIAL',15))
        self.entryDni.grid(column=1,row=2, padx=10, pady=5, columnspan=2)

        self.svFechaNacimiento = tk.StringVar()
        self.entryFechaNacimiento = tk.Entry(self, textvariable=self.svFechaNacimiento)
        self.entryFechaNacimiento.config(width=50,font=('ARIAL',15))
        self.entryFechaNacimiento.grid(column=1,row=3, padx=10, pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50,font=('ARIAL',15))
        self.entryEdad.grid(column=1,row=4, padx=10, pady=5, columnspan=2)

        self.svAntecedentes = tk.StringVar()
        self.entryAntecedentes = tk.Entry(self, textvariable=self.svAntecedentes)
        self.entryAntecedentes.config(width=50,font=('ARIAL',15))
        self.entryAntecedentes.grid(column=1,row=5, padx=10, pady=5, columnspan=2)

        self.svHijos = tk.StringVar()
        self.entryHijos = tk.Entry(self, textvariable=self.svHijos)
        self.entryHijos.config(width=50,font=('ARIAL',15))
        self.entryHijos.grid(column=1,row=6, padx=10, pady=5, columnspan=2)

        self.svOcupacion = tk.StringVar()
        self.entryOcupacion = tk.Entry(self, textvariable=self.svOcupacion)
        self.entryOcupacion.config(width=50,font=('ARIAL',15))
        self.entryOcupacion.grid(column=1,row=7, padx=10, pady=5, columnspan=2)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50,font=('ARIAL',15))
        self.entryTelefono.grid(column=1,row=8, padx=10, pady=5, columnspan=2)

        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=50,font=('ARIAL',15))
        self.entryCorreo.grid(column=1,row=9, padx=10, pady=5, columnspan=2)

        #BUTTONS
        self.btnNuevo = tk.Button(self, text='Nuevo',command=self.habilitar)
        self.btnNuevo.config(width=20, font=('ARIAL',12,'bold'),fg='#253c42', bg="#e6e6e7", cursor='hand2', activebackgroun='#35bd6f')
        self.btnNuevo.grid(column=0, row=10, pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar', command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('ARIAL',12,'bold'),fg='#253c42', bg="#e6e6e7",cursor='hand2', activebackgroun='#35bd6f')
        self.btnGuardar.grid(column=1, row=10, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar',command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('ARIAL',12,'bold'),fg='#253c42', bg="#e6e6e7",cursor='hand2', activebackgroun='#35bd6f')
        self.btnCancelar.grid(column=2, row=10, pady=5)

        #BUSCADOR
        #LABEL BUSCADOR
        self.lblBuscarDni = tk.Label(self, text='Buscar DNI: ')
        self.lblBuscarDni.config(font=('ARIAL',15,'bold'),bg='#407e5e',fg='#ffffff')
        self.lblBuscarDni.grid(column=3, row=0, padx=10,pady=5)

        self.lblBuscarApellido = tk.Label(self, text='Buscar Apellido: ')
        self.lblBuscarApellido.config(font=('ARIAL',15,'bold'),bg='#407e5e',fg='#ffffff')
        self.lblBuscarApellido.grid(column=3, row=1, padx=10,pady=5)

        #ENTRYS BUSCADOR
        self.svBuscarDni = tk.StringVar()
        self.entryBuscarDni = tk.Entry(self,textvariable=self.svBuscarDni)
        self.entryBuscarDni.config(width=20,font=('ARIAL',15))
        self.entryBuscarDni.grid(column=4,row=0, padx=10, pady=5, columnspan=2)

        self.svBuscarApellido = tk.StringVar()
        self.entryBuscarApellido = tk.Entry(self,textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.config(width=20,font=('ARIAL',15))
        self.entryBuscarApellido.grid(column=4,row=1, padx=10, pady=5, columnspan=2)

        #BUTTON BUSCADOR
        self.btnBuscarCondicion = tk.Button(self, text='Buscar', command=self.buscarCondicion)
        self.btnBuscarCondicion.config(width=20, font=('ARIAL',12,'bold'),fg='#FFFFFF', bg="#8F21FF",cursor='hand2', activebackgroun='#C79DF2')
        self.btnBuscarCondicion.grid(column=3, row=2, padx=10, pady=5, columnspan=1)
        
        self.btnLimpiarBuscador = tk.Button(self, text='Limpiar', command=self.limpiarBuscador)
        self.btnLimpiarBuscador.config(width=20, font=('ARIAL',12,'bold'),fg='#FFFFFF', bg="#8F21FF",cursor='hand2', activebackgroun='#C79DF2')
        self.btnLimpiarBuscador.grid(column=4, row=2, padx=10, pady=5, columnspan=1)

        #BUTTON CALENDARIO
        self.btnCalendario = tk.Button(self, text='Calendario', command=self.vistaCalendario)
        self.btnCalendario.config(width=12, font=('ARIAL',12,'bold'),fg='#FFFFFF', bg="#0CC6C2",cursor='hand2', activebackgroun='#C774CF')
        self.btnCalendario.grid(column=3, row=4, padx=10, pady=5, columnspan=1)

    def vistaCalendario(self):
        self.calendario = Toplevel()
        self.calendario.title("FECHA NACIMIENTO")
        self.calendario.resizable(0,0)
        self.calendario.config(bg='#407e5e')

        self.svCalendario = tk.StringVar()
        self.calendar = tc.Calendar(self.calendario,selectmode='day', year=1990, month=1, day=1, locale='es_US',bg='#777777',fg='#ffffff', headersbackground='#B6DDFE',textvariable=self.svCalendario,cursor='hand2',date_pattern='dd-mm-Y')
        self.calendar.pack(pady=22)
        self.calendar.grid(row=1, column=0)

        #TRACE ENVIAR FECHA
        self.svCalendario.trace('w', self.enviarFecha)

    def enviarFecha(self, *args):
        self.svFechaNacimiento.set('' + self.svCalendario.get())
        if len(self.calendar.get_date()) > 1:
            self.svCalendario.trace('w', self.calcularEdad)

    def calcularEdad(self, *args):
        self.fechaActual = date.today()
        self.date1 = self.calendar.get_date()
        self.conver = datetime.strptime(self.date1, "%d-%m-%Y")

        self.resul = self.fechaActual.year - self.conver.year
        self.resul -= ((self.fechaActual.month,self.fechaActual.day) < (self.conver.month,self.conver.day))
        self.svEdad.set(self.resul)

    def limpiarBuscador(self):
        self.svBuscarApellido.set('')
        self.svBuscarDni.set('')
        self.tablaPaciente()

    def buscarCondicion(self):
        if len(self.svBuscarDni.get()) > 0 or len(self.svBuscarApellido.get()) > 0:
            where = "WHERE 1=1"
            if (len(self.svBuscarDni.get())) > 0:
                where = "WHERE dni = " + self.svBuscarDni.get() + "" #WHERE dni = '87878787'
            if (len(self.svBuscarApellido.get())) > 0:
                where = "WHERE Apellido LIKE  '" + self.svBuscarApellido.get() + "%' AND activo = 1"
            
            self.tablaPaciente(where)
        else:
            self.tablaPaciente()



    def guardarPaciente(self):
        persona = Persona(
            self.svNombre.get(), self.svApellido.get(), self.svDni.get(), self.svFechaNacimiento.get(), self.svEdad.get(), 
            self.svAntecedentes.get(), self.svHijos.get(), self.svOcupacion.get(), self.svTelefono.get(), self.svCorreo.get()
        )

        if self.idPersona == None:
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)

        self.deshabilitar()
        self.tablaPaciente()
    
    def habilitar(self):
        #self.idPersona = None
        self.svNombre.set('')
        self.svApellido.set('')
        self.svDni.set('')
        self.svFechaNacimiento.set('')
        self.svEdad.set('')
        self.svAntecedentes.set('')
        self.svHijos.set('')
        self.svOcupacion.set('')
        self.svTelefono.set('')
        self.svCorreo.set('')

        self.entryNombre.config(state='normal')
        self.entryApellido.config(state='normal')
        self.entryDni.config(state='normal')
        self.entryFechaNacimiento.config(state='normal')
        self.entryEdad.config(state='normal')
        self.entryAntecedentes.config(state='normal')
        self.entryHijos.config(state='normal')
        self.entryOcupacion.config(state='normal')
        self.entryTelefono.config(state='normal')
        self.entryCorreo.config(state='normal')

        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')
        self.btnCalendario.config(state='normal')

    def deshabilitar(self):
        self.idPersona = None
        self.svNombre.set('')
        self.svApellido.set('')
        self.svDni.set('')
        self.svFechaNacimiento.set('')
        self.svEdad.set('')
        self.svAntecedentes.set('')
        self.svHijos.set('')
        self.svOcupacion.set('')
        self.svTelefono.set('')
        self.svCorreo.set('')

        self.entryNombre.config(state='disabled')
        self.entryApellido.config(state='disabled')
        self.entryDni.config(state='disabled')
        self.entryFechaNacimiento.config(state='disabled')
        self.entryEdad.config(state='disabled')
        self.entryAntecedentes.config(state='disabled')
        self.entryHijos.config(state='disabled')
        self.entryOcupacion.config(state='disabled')
        self.entryTelefono.config(state='disabled')
        self.entryCorreo.config(state='disabled')

        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')
        self.btnCalendario.config(state='disabled')

    def tablaPaciente(self, where=""):

        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listar()
            #self.listaPersona.reverse()

        self.tabla = ttk.Treeview(self, column=('Nombre','Apellido','Dni','FechaNacimiento','Edad','Antecedentes','Hijos','Ocupacion','Telefono','Correo'))
        self.tabla.grid(column=0, row=11, columnspan=12, sticky='nse')
        self.scroll = ttk.Scrollbar(self,orient='vertical',command=self.tabla.yview)
        self.scroll.grid(column=12, row=11, sticky='nse')

        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.tag_configure('evenrow', background='#c5eafe')

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Apellido')
        self.tabla.heading('#3', text='Dni')
        self.tabla.heading('#4', text='FechaNacimiento')
        self.tabla.heading('#5', text='Edad')
        self.tabla.heading('#6', text='Antecedentes')
        self.tabla.heading('#7', text='Hijos')
        self.tabla.heading('#8', text='Ocupacion')
        self.tabla.heading('#9', text='Telefono')
        self.tabla.heading('#10', text='Correo')

        self.tabla.column("#0", anchor=W, width=50)
        self.tabla.column("#1", anchor=W, width=150)
        self.tabla.column("#2", anchor=W, width=120)
        self.tabla.column("#3", anchor=W, width=80)
        self.tabla.column("#4", anchor=W, width=80)
        self.tabla.column("#5", anchor=W, width=40)
        self.tabla.column("#6", anchor=W, width=220)
        self.tabla.column("#7", anchor=W, width=50)
        self.tabla.column("#8", anchor=W, width=300)
        self.tabla.column("#9", anchor=W, width=85)
        self.tabla.column("#10", anchor=W, width=170)

        for p in self.listaPersona:
            self.tabla.insert('',0,text=p[0],values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10]),tags=('evenrow',))

        self.btnEditarPaciente = tk.Button(self, text='Editar Paciente', command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20,font=('ARIAL',12,'bold'),fg='#DAD5D6',bg='#1e0075', activebackground='#9379E0', cursor='hand2')
        self.btnEditarPaciente.grid(row=12, column=0, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command=self.eliminarDatoPaciente)
        self.btnEliminarPaciente.config(width=20,font=('ARIAL',12,'bold'),fg='#DAD5D6',bg='#1e0075', activebackground='#9379E0', cursor='hand2')
        self.btnEliminarPaciente.grid(row=12, column=1, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text='Historial Paciente', command=self.historiaClinica)
        self.btnHistorialPaciente.config(width=20,font=('ARIAL',12,'bold'),fg='#DAD5D6',bg='#1e0075', activebackground='#9379E0', cursor='hand2')
        self.btnHistorialPaciente.grid(row=12, column=2, padx=10, pady=5)

        self.btnSalir = tk.Button(self, text='Salir', command=self.root.destroy)
        self.btnSalir.config(width=20,font=('ARIAL',12,'bold'),fg='#DAD5D6',bg='#434343', activebackground='#5A5A5A', cursor='hand2')
        self.btnSalir.grid(row=12, column=4, padx=10, pady=5)

    def historiaClinica(self):

        try:
            if self.idPersona == None:
                self.idPersona = self.tabla.item(self.tabla.selection())['text']
                self.idPersonaHistoria = self.tabla.item(self.tabla.selection())['text']
            if (self.idPersona > 0  ):
                idPersona = self.idPersona
            
            self.topHistoriaClinica = Toplevel()
            self.topHistoriaClinica.title('HISTORIAL CLINICO')
            self.topHistoriaClinica.resizable(0,0)
            self.topHistoriaClinica.config(bg='#CDD8FF')
            
            self.listaHistoria = listarHistoria(idPersona)
            self.tablaHistoria = ttk.Treeview(self.topHistoriaClinica, column=('Nombre Completo', 'Fecha Historia', 'Motivo De Consulta', 'Tipo De Alimentacion', 'Actividad Fisica', 'Digestion', 'Medicacion', 'Operaciones/Cicatrices', 'Embarazos', 'Traumatismos', 'Observaciones'))
            self.tablaHistoria.grid(row=0, column=0, columnspan=12, sticky='nse')

            self.scrollHistoria = ttk.Scrollbar(self.topHistoriaClinica, orient='vertical', command=self.tablaHistoria.yview)
            self.scrollHistoria.grid(row=0, column=13, sticky='nse')

            self.tablaHistoria.configure(yscrollcommand=self.scrollHistoria.set)

            self.tablaHistoria.heading('#0', text='ID')
            self.tablaHistoria.heading('#1', text='Nombre Completo')
            self.tablaHistoria.heading('#2', text='Fecha y Hora')
            self.tablaHistoria.heading('#3', text='Motivo de Consulta')
            self.tablaHistoria.heading('#4', text='Tipo De Alimentacion')
            self.tablaHistoria.heading('#5', text='Actividad Fisica')
            self.tablaHistoria.heading('#6', text='Digestion')
            self.tablaHistoria.heading('#7', text='Medicacion')
            self.tablaHistoria.heading('#8', text='Operaciones/Cicatrices')
            self.tablaHistoria.heading('#9', text='Embarazos')
            self.tablaHistoria.heading('#10', text='Traumatismos')
            self.tablaHistoria.heading('#11', text='Observaciones')
            
            self.tablaHistoria.column('#0', anchor=W, width=30)
            self.tablaHistoria.column('#1', anchor=W, width=130)
            self.tablaHistoria.column('#2', anchor=W, width=100)
            self.tablaHistoria.column('#3', anchor=W, width=220)
            self.tablaHistoria.column('#4', anchor=W, width=100)
            self.tablaHistoria.column('#5', anchor=W, width=100)
            self.tablaHistoria.column('#6', anchor=W, width=80)
            self.tablaHistoria.column('#7', anchor=W, width=80)
            self.tablaHistoria.column('#8', anchor=W, width=80)
            self.tablaHistoria.column('#9', anchor=W, width=70)
            self.tablaHistoria.column('#10', anchor=W, width=80)
            self.tablaHistoria.column('#11', anchor=W, width=450)

            for p in self.listaHistoria:
                self.tablaHistoria.insert('',0, text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11]))
            
            self.btnGuardarHistoria = tk.Button(self.topHistoriaClinica, text='Agregar Historia', command=self.topAgregarHistoria)
            self.btnGuardarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#002771', cursor='hand2',activebackground='#7198E0')
            self.btnGuardarHistoria.grid(row=2,column=0, padx=10, pady=5)
            
            self.btnEditarHistoria = tk.Button(self.topHistoriaClinica, text='Editar Historia', command=self.topEditarHistorialClinico)
            self.btnEditarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#002771', cursor='hand2',activebackground='#7198E0')
            self.btnEditarHistoria.grid(row=2,column=1, padx=10, pady=5)

            self.btnEliminarHistoria = tk.Button(self.topHistoriaClinica, text='Eliminar Historia',command=self.eliminarHistorialClinico)
            self.btnEliminarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#002771', cursor='hand2',activebackground='#7198E0')
            self.btnEliminarHistoria.grid(row=2,column=2, padx=10, pady=5)

            self.btnSalirHistoria = tk.Button(self.topHistoriaClinica, text='Salir', command=self.salirTop)
            self.btnSalirHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#002771', cursor='hand2',activebackground='#7198E0')
            self.btnSalirHistoria.grid(row=2,column=6, padx=10, pady=5)

            self.idPersona = None
        
        except Exception as ex:
            print('EXCEPT = {}'.format(ex))
            title = 'Historia Clinica'
            mensaje = 'Error al mostrar historial'
            print(self.idPersona)
            messagebox.showerror(title,mensaje)

    def topAgregarHistoria(self):
        self.topAHistoria = Toplevel()
        self.topAHistoria.title('AGREGAR HISTORIA')
        self.topAHistoria.resizable(0,0)
        self.topAHistoria.config(bg='#CDD8FF')
        #FRAME 1
        self.frameDatosHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameDatosHistoria.config(bg='#CDD8FF')
        self.frameDatosHistoria.pack(fill="both",expand="yes",pady=10,padx=20)

        #LABELS AGREGAR HISTORIA CLINICA
        self.lblMotivoHistoria = tk.Label(self.frameDatosHistoria, text='Motivo de la Consulta', width=30, font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblMotivoHistoria.grid(row=0, column=0, padx=5, pady=3)
        
        self.lblAlimentacion = tk.Label(self.frameDatosHistoria, text='Tipo de Alimentacion', width=20, font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblAlimentacion.grid(row=2, column=0, padx=5, pady=3)
        
        self.lblActividadFisica = tk.Label(self.frameDatosHistoria, text='Actividad Fisica', width=20, font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblActividadFisica.grid(row=4, column=0, padx=5, pady=3)
        
        self.lblDigestion = tk.Label(self.frameDatosHistoria, text='Digestion', width=20, font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblDigestion.grid(row=6, column=0, padx=5, pady=3)
        
        self.lblMedicacion = tk.Label(self.frameDatosHistoria, text='Medicacion', width=20, font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblMedicacion.grid(row=8, column=0, padx=5, pady=3)
        
        self.lblOperacionesCicatrices = tk.Label(self.frameDatosHistoria, text='Operaciones/Cicatrices', width=20, font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblOperacionesCicatrices.grid(row=10, column=0, padx=5, pady=3)
        
        self.lblEmbarazos = tk.Label(self.frameDatosHistoria, text='Embarazos', width=20, font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblEmbarazos.grid(row=12, column=0, padx=5, pady=3)
        
        self.lblTraumatismos = tk.Label(self.frameDatosHistoria, text='Traumatismos', width=20, font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblTraumatismos.grid(row=14, column=0, padx=5, pady=3)
        
        self.lblObservaciones = tk.Label(self.frameDatosHistoria, text='Observaciones', width=30, font=('ARIAL',15,'bold'),bg='#CDD8FF')
        self.lblObservaciones.grid(row=16, column=0, padx=5, pady=3)
        
        #ENTRYS AGREGAR HISTORIA CLINICA
        self.svMotivoHistoria = tk.StringVar()
        self.motivoHistoria = tk.Entry(self.frameDatosHistoria,textvariable=self.svMotivoHistoria)
        self.motivoHistoria.config(width=64, font=('ARIAL',15))
        self.motivoHistoria.grid(row=1,column=0,padx=5,pady=3,columnspan=2)
        
        self.svAlimentacion = tk.StringVar()
        self.alimentacion = tk.Entry(self.frameDatosHistoria,textvariable=self.svAlimentacion)
        self.alimentacion.config(width=64, font=('ARIAL',15))
        self.alimentacion.grid(row=3,column=0,padx=5,pady=3,columnspan=2)
        
        self.svActividadFisica = tk.StringVar()
        self.actividadFisica = tk.Entry(self.frameDatosHistoria,textvariable=self.svActividadFisica)
        self.actividadFisica.config(width=64, font=('ARIAL',15))
        self.actividadFisica.grid(row=5,column=0,padx=5,pady=3,columnspan=2)
        
        self.svDigestion = tk.StringVar()
        self.digestion = tk.Entry(self.frameDatosHistoria,textvariable=self.svDigestion)
        self.digestion.config(width=64, font=('ARIAL',15))
        self.digestion.grid(row=7,column=0,padx=5,pady=3,columnspan=2)
        
        self.svMedicacion = tk.StringVar()
        self.medicacion = tk.Entry(self.frameDatosHistoria,textvariable=self.svMedicacion)
        self.medicacion.config(width=64, font=('ARIAL',15))
        self.medicacion.grid(row=9,column=0,padx=5,pady=3,columnspan=2)
        
        self.svOperacionesCicatrices = tk.StringVar()
        self.operacionesCicatrices = tk.Entry(self.frameDatosHistoria,textvariable=self.svOperacionesCicatrices)
        self.operacionesCicatrices.config(width=64, font=('ARIAL',15))
        self.operacionesCicatrices.grid(row=11,column=0,padx=5,pady=3,columnspan=2)
        
        self.svEmbarazos = tk.StringVar()
        self.embarazos = tk.Entry(self.frameDatosHistoria,textvariable=self.svEmbarazos)
        self.embarazos.config(width=64, font=('ARIAL',15))
        self.embarazos.grid(row=13,column=0,padx=5,pady=3,columnspan=2)
        
        self.svTraumatismos = tk.StringVar()
        self.traumatismos = tk.Entry(self.frameDatosHistoria,textvariable=self.svTraumatismos)
        self.traumatismos.config(width=64, font=('ARIAL',15))
        self.traumatismos.grid(row=15,column=0,padx=5,pady=3,columnspan=2)
        
        self.svObservaciones = tk.StringVar()
        self.observaciones = tk.Entry(self.frameDatosHistoria,textvariable=self.svObservaciones)
        self.observaciones.config(width=64, font=('ARIAL',15))
        self.observaciones.grid(row=17,column=0,padx=5,pady=3,columnspan=2)

        #FRAME 2
        self.frameFechaHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameFechaHistoria.config(bg='#CDD8FF')
        self.frameFechaHistoria.pack(fill="both",expand="yes", padx=20, pady=10)

        #LABEL FECHA AGREGAR HISTORIA
        self.lblFechaHistoria = tk.Label(self.frameFechaHistoria, text='Fecha y Hora', width=20, font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblFechaHistoria.grid(row=1, column=0, padx=5, pady=3)

        #ENTRY FECHA AGREGAR HISTORIA
        self.svFechaHistoria = tk.StringVar()
        self.entryFechaHistoria = tk.Entry(self.frameFechaHistoria, textvariable=self.svFechaHistoria)
        self.entryFechaHistoria.config(width=20, font=('ARIAL',15))
        self.entryFechaHistoria.grid(row=1, column=1, padx=5, pady=3)
        #TRAER FECHA Y HORA ACTUAL
        self.svFechaHistoria.set(datetime.today().strftime('%d-%m-%Y %H:%M'))

        #BUTTONS AGREGAR HISTORIA
        self.btnAgregarHistoria = tk.Button(self.frameFechaHistoria, text='Agregar Historia', command=self.agregarHistorialMedico)
        self.btnAgregarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000992', cursor='hand2', activebackground='#4E56C6')
        self.btnAgregarHistoria.grid(row=2, column=0, padx=10, pady=5)

        self.btnSalirAgregarHistoria = tk.Button(self.frameFechaHistoria, text='Salir',command=self.topAHistoria.destroy)
        self.btnSalirAgregarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2', activebackground='#646464')
        self.btnSalirAgregarHistoria.grid(row=2, column=3, padx=10, pady=5)

    def agregarHistorialMedico(self):
        try:
            if self.idHistoriaClinica == None:
                guardarHistoria(self.idPersonaHistoria, self.svFechaHistoria.get(), self.svMotivoHistoria.get(), self.svAlimentacion.get(), self.svActividadFisica.get(), self.svDigestion.get(), self.svMedicacion.get(), self.svOperacionesCicatrices.get(), self.svEmbarazos.get(), self.traumatismos.get(), self.observaciones.get())
            self.topAHistoria.destroy()
            self.topHistoriaClinica.destroy()
            self.idPersona = None
        except:
            title = 'Agregar Historia'
            mensaje = 'Error al agregar historia clinica'
            messagebox.showerror(title, mensaje)

    def eliminarHistorialClinico(self):
        try:
            self.idHistoriaClinica = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
            eliminarHistoria(self.idHistoriaClinica)

            self.idHistoriaClinica = None
            self.topHistoriaClinica.destroy()
        except:
            title = 'Eliminar Historia'
            mensaje = 'Error al eliminar'
            messagebox.showerror(title,mensaje)

    def topEditarHistorialClinico(self):
        try:
            self.idHistoriaClinica = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
            self.fechaHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][1]
            self.motivoHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][2]
            self.alimentacionHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][3]
            self.actividadFisicaHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][4]
            self.digestionHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][5]
            self.medicacionHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][6]
            self.operacionesCicatricesHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][7]
            self.embarazosHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][8]
            self.traumatismosHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][9]
            self.observacionesHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][10]

            self.topEditarHistoria = Toplevel()
            self.topEditarHistoria.title('EDITAR HISTORIA CLINICA')
            self.topEditarHistoria.resizable(0,0)
            self.topEditarHistoria.config(bg='#CDD8FF')

            #FRAME EDITAR DATOS HISTORIA
            self.frameEditarHistoria = tk.LabelFrame(self.topEditarHistoria)
            self.frameEditarHistoria.config(bg='#CDD8FF')
            self.frameEditarHistoria.pack(fill="both", expand="yes", padx=20, pady=10)

            #LABEL EDITAR HISTORIA
            self.lblMotivoEditar = tk.Label(self.frameEditarHistoria, text='Motivo de la Historia', width=30, font=('ARIAL',15,'bold'), bg='#CDD8FF')
            self.lblMotivoEditar.grid(row=0,column=0, padx=5, pady=3)

            self.lblAlimentacionEditar = tk.Label(self.frameEditarHistoria, text='Tipo de Alimentacion', width=30, font=('ARIAL',15,'bold'), bg='#CDD8FF')
            self.lblAlimentacionEditar.grid(row=2,column=0, padx=5, pady=3)

            self.lblActividadFisicaEditar = tk.Label(self.frameEditarHistoria, text='Actividad Fisica', width=30, font=('ARIAL',15,'bold'), bg='#CDD8FF')
            self.lblActividadFisicaEditar.grid(row=4,column=0, padx=5, pady=3)

            self.lblDigestionEditar = tk.Label(self.frameEditarHistoria, text='Digestion', width=30, font=('ARIAL',15,'bold'), bg='#CDD8FF')
            self.lblDigestionEditar.grid(row=6,column=0, padx=5, pady=3)

            self.lblMedicacionEditar = tk.Label(self.frameEditarHistoria, text='Medicacion', width=30, font=('ARIAL',15,'bold'), bg='#CDD8FF')
            self.lblMedicacionEditar.grid(row=8,column=0, padx=5, pady=3)

            self.lblOperacionesCicatricesEditar = tk.Label(self.frameEditarHistoria, text='Operaciones/Cicatrices', width=30, font=('ARIAL',15,'bold'), bg='#CDD8FF')
            self.lblOperacionesCicatricesEditar.grid(row=10,column=0, padx=5, pady=3)

            self.lblEmbarazosEditar = tk.Label(self.frameEditarHistoria, text='Embarazos', width=30, font=('ARIAL',15,'bold'), bg='#CDD8FF')
            self.lblEmbarazosEditar.grid(row=12,column=0, padx=5, pady=3)

            self.lblTraumatismosEditar = tk.Label(self.frameEditarHistoria, text='Traumatismos', width=30, font=('ARIAL',15,'bold'), bg='#CDD8FF')
            self.lblTraumatismosEditar.grid(row=14,column=0, padx=5, pady=3)

            self.lblObservacionesEditar = tk.Label(self.frameEditarHistoria, text='Observaciones', width=30, font=('ARIAL',15,'bold'), bg='#CDD8FF')
            self.lblObservacionesEditar.grid(row=16,column=0, padx=5, pady=3)

            #ENTRYS EDITAR HISTORIA

            self.svMotivoEditar = tk.StringVar()
            self.entryMotivoEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svMotivoEditar)
            self.entryMotivoEditar.config(width=65, font=('ARIAL',15))
            self.entryMotivoEditar.grid(row=1, column=0, pady=3, padx=5,columnspan=2)
            
            self.svAlimentacionEditar = tk.StringVar()
            self.entryAlimentacionEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svAlimentacionEditar)
            self.entryAlimentacionEditar.config(width=65, font=('ARIAL',15))
            self.entryAlimentacionEditar.grid(row=3, column=0, pady=3, padx=5,columnspan=2)

            self.svActividadFisicaEditar = tk.StringVar()
            self.entryActividadFisicaEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svActividadFisicaEditar)
            self.entryActividadFisicaEditar.config(width=65, font=('ARIAL',15))
            self.entryActividadFisicaEditar.grid(row=5, column=0, pady=3, padx=5,columnspan=2)

            self.svDigestionEditar = tk.StringVar()
            self.entryDigestionEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svDigestionEditar)
            self.entryDigestionEditar.config(width=65, font=('ARIAL',15))
            self.entryDigestionEditar.grid(row=7, column=0, pady=3, padx=5,columnspan=2)

            self.svMedicacionEditar = tk.StringVar()
            self.entryMedicacionEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svMedicacionEditar)
            self.entryMedicacionEditar.config(width=65, font=('ARIAL',15))
            self.entryMedicacionEditar.grid(row=9, column=0, pady=3, padx=5,columnspan=2)

            self.svOperacionesCicatricesEditar = tk.StringVar()
            self.entryOperacionesCicatricesEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svOperacionesCicatricesEditar)
            self.entryOperacionesCicatricesEditar.config(width=65, font=('ARIAL',15))
            self.entryOperacionesCicatricesEditar.grid(row=11, column=0, pady=3, padx=5,columnspan=2)

            self.svEmbarazosEditar = tk.StringVar()
            self.entryEmbarazosEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svEmbarazosEditar)
            self.entryEmbarazosEditar.config(width=65, font=('ARIAL',15))
            self.entryEmbarazosEditar.grid(row=13, column=0, pady=3, padx=5,columnspan=2)

            self.svTraumatismosEditar = tk.StringVar()
            self.entryTraumatismosEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svTraumatismosEditar)
            self.entryTraumatismosEditar.config(width=65, font=('ARIAL',15))
            self.entryTraumatismosEditar.grid(row=15, column=0, pady=3, padx=5,columnspan=2)

            self.svObservacionesEditar = tk.StringVar()
            self.entryObservacionesEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svObservacionesEditar)
            self.entryObservacionesEditar.config(width=65, font=('ARIAL',15))
            self.entryObservacionesEditar.grid(row=17, column=0, pady=3, padx=5,columnspan=2)

            #FRAME FECHA EDITAR
            self.frameFechaEditar = tk.LabelFrame(self.topEditarHistoria)
            self.frameFechaEditar.config(bg='#CDD8FF')
            self.frameFechaEditar.pack(fill="both", expand="yes", padx=20, pady=10)

            #LABEL FECHA EDITAR
            self.lblFechaHistoriaEditar = tk.Label(self.frameFechaEditar, text='Fecha y Hora', width=30, font=('ARIAL',15,'bold'), bg='#CDD8FF')
            self.lblFechaHistoriaEditar.grid(row=1,column=0, padx=5, pady=3)

            #ENTRY FECHA EDITAR
            self.svFechaHistoriaEditar = tk.StringVar()
            self.entryFechaHistoriaEditar = tk.Entry(self.frameFechaEditar, textvariable=self.svFechaHistoriaEditar)
            self.entryFechaHistoriaEditar.config(width=20, font=('ARIAL',15))
            self.entryFechaHistoriaEditar.grid(row=1, column=1, pady=3, padx=5)

            #INSERTAR LOS VALORES A LOS ENTRYS
            self.entryMotivoEditar.insert(0,self.motivoHistoriaEditar)
            self.entryAlimentacionEditar.insert(0,self.alimentacionHistoriaEditar)
            self.entryActividadFisicaEditar.insert(0, self.actividadFisicaHistoriaEditar)
            self.entryDigestionEditar.insert(0, self.digestionHistoriaEditar)
            self.entryMedicacionEditar.insert(0,self.medicacionHistoriaEditar)
            self.entryOperacionesCicatricesEditar.insert(0,self.medicacionHistoriaEditar)
            self.entryEmbarazosEditar.insert(0,self.embarazosHistoriaEditar)
            self.entryTraumatismosEditar.insert(0,self.traumatismosHistoriaEditar)
            self.entryObservacionesEditar.insert(0,self.observacionesHistoriaEditar)
            self.entryFechaHistoriaEditar.insert(0,self.fechaHistoriaEditar)

            #BUTTON EDITAR HISTORIA
            self.btnEditarHistoriaClinica = tk.Button(self.frameFechaEditar,text='Editar Historia', command=self.historiaClinicaEditar)
            self.btnEditarHistoriaClinica.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#030058', cursor='hand2', activebackground='#8986DA')
            self.btnEditarHistoriaClinica.grid(row=2, column=0, padx=10, pady=5)

            self.btnSalirEditarHistoriaClinica = tk.Button(self.frameFechaEditar,text='Salir', command=self.topEditarHistoria.destroy)
            self.btnSalirEditarHistoriaClinica.config(width=20, font=('ARIAL',12,'bold'),fg='#DAD5D6',bg='#000000', cursor='hand2', activebackground='#676767')
            self.btnSalirEditarHistoriaClinica.grid(row=2, column=1, padx=10, pady=5)

            if self.idHistoriaClinicaEditar == None:
                self.idHistoriaClinicaEditar = self.idHistoriaClinica

            self.idHistoriaClinica = None
        except Exception as ex:
            print('EXCEPT = {}'.format(ex))
            title = 'Editar Historia'
            mensaje = 'Error al editar historia'
            #print(self.idPersona)
            messagebox.showerror(title,mensaje)
    
    def historiaClinicaEditar(self):
        try:
            editarHistoria(self.svFechaHistoriaEditar.get(), self.svMotivoEditar.get(), self.svAlimentacionEditar.get(), self.svActividadFisicaEditar.get(), self.svDigestionEditar.get(), self.svMedicacionEditar.get(), self.svOperacionesCicatricesEditar.get(), self.svEmbarazosEditar.get(), self.svTraumatismosEditar.get(), self.svObservacionesEditar.get(), self.idHistoriaClinicaEditar)
            self.idHistoriaClinicaEditar = None
            self.idHistoriaClinica = None
            self.topEditarHistoria.destroy()
            self.topHistoriaClinica.destroy()
        except Exception as ex:
            print('EXCEPT = {}'.format(ex))
            title = 'Editar Historia'
            mensaje = 'Error al editar historia'
            messagebox.showerror(title,mensaje)
            self.topEditarHistoria.destroy()



    def salirTop(self):
        self.topHistoriaClinica.destroy()

    def editarPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text'] #Trae el ID
            self.nombrePaciente = self.tabla.item(self.tabla.selection())['values'][0] 
            self.apellidoPaciente = self.tabla.item(self.tabla.selection())['values'][1] 
            self.dniPaciente = self.tabla.item(self.tabla.selection())['values'][2]
            self.fechaNacimientoPaciente = self.tabla.item(self.tabla.selection())['values'][3]
            self.edadPaciente = self.tabla.item(self.tabla.selection())['values'][4]
            self.antecedentesPaciente = self.tabla.item(self.tabla.selection())['values'][5]
            self.hijosPaciente = self.tabla.item(self.tabla.selection())['values'][6]
            self.ocupacionPaciente = self.tabla.item(self.tabla.selection())['values'][7]
            self.telefonoPaciente = self.tabla.item(self.tabla.selection())['values'][8]
            self.correoPaciente = self.tabla.item(self.tabla.selection())['values'][9]

            self.habilitar()

            self.entryNombre.insert(0, self.nombrePaciente)
            self.entryApellido.insert(0, self.apellidoPaciente)
            self.entryDni.insert(0, self.dniPaciente)
            self.entryFechaNacimiento.insert(0, self.fechaNacimientoPaciente)
            self.entryEdad.insert(0, self.edadPaciente)
            self.entryAntecedentes.insert(0, self.antecedentesPaciente)
            self.entryHijos.insert(0, self.hijosPaciente)
            self.entryOcupacion.insert(0, self.ocupacionPaciente)
            self.entryTelefono.insert(0, self.telefonoPaciente)
            self.entryCorreo.insert(0, self.correoPaciente)
        except:
            title = 'Editar Paciente'
            mensaje = 'Error al editar paciente'
            messagebox.showerror(title,mensaje)

    def eliminarDatoPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text']
            eliminarPaciente(self.idPersona)

            self.tablaPaciente()
            self.idPersona = None
        except:
            title = 'Eliminar Paciente'
            mensaje = 'No se pudo eliminar paciente'
            messagebox.showinfo(title,mensaje)


