# INTERGAZ GRAFICA
import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel, LabelFrame
from modelo.pacienteDao import Persona, guardarDatoPaciente, listarCondicion, listar

class Frame(tk.Frame):
    def __init__(self,root):
        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#407e5e')  #7bbe9b
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
    
    def guardarPaciente(self):
        persona = Persona(
            self.svNombre.get(), self.svApellido.get(), self.svDni.get(), self.svFechaNacimiento.get(), self.svEdad.get(), 
            self.svAntecedentes.get(), self.svHijos.get(), self.svOcupacion.get(), self.svTelefono.get(), self.svCorreo.get()
        )

        guardarDatoPaciente(persona)
        self.deshabilitar()
    
    def habilitar(self):
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

    def deshabilitar(self):
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

    def tablaPaciente(self, where=""):

        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listar()

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