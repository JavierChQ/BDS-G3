from tkinter import *
from tkinter.ttk import Treeview
import mysql.connector

class Empleados:
    # METODO CONSTRUCTOR
    def __init__(self,app):
        # INTERFAZ
        # Ventana principal
        self.app = app
        self.app.title('Gestion de empleados')
        self.app.geometry('640x380')

        # 0. Conexion a la base de datos
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'mysqljavier',
            database = 'db_practica_datag3'
        )
        self.cursor = self.db.cursor
        
        # 1. Contenedor
        frame = LabelFrame(self.app,text='Registro de empleados')
        frame.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

        # 1.1. Formulario
        lbl_dni = Label(frame,text='DNI')
        lbl_dni.grid(row=0,column=0,padx=10,pady=5)
        self.txt_dni = Entry(frame)
        self.txt_dni.grid(row=0,column=1)

        lbl_nombre = Label(frame,text='NOMBRE')
        lbl_nombre.grid(row=0,column=2,padx=10,pady=5)
        self.txt_nombre = Entry(frame)
        self.txt_nombre.grid(row=0,column=3)

        # 2. Tabla
        self.tree = Treeview(self.app,columns=('dni','nombre'))
        self.tree.heading('#0',text='ID')
        self.tree.heading('dni',text='DNI')
        self.tree.heading('nombre',text='NOMBRE')
        self.tree.grid(row=1,column=0,padx=20,pady=10)