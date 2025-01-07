from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
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
        self.cursor = self.db.cursor()

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

        # 1.2. Boton imsertar
        self.btn_insertar = Button(frame,text='Insertar nuevo empleado', command=self.insertar)
        self.btn_insertar.grid(row=0,column=4,padx=10,pady=5)

        # 2. Tabla
        self.tree = Treeview(self.app,columns=('dni','nombre'))
        self.tree.heading('#0',text='ID')
        self.tree.heading('dni',text='DNI')
        self.tree.heading('nombre',text='NOMBRE')
        self.tree.grid(row=1,column=0,padx=20,pady=10)

        self.cargar_empleados()
    # METODOS
    def cargar_empleados(self):
        # Limpiar arbol antes de cargar datos
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Consulat SQL para selccionar las columnas de la tabla
        self.cursor.execute("select id,dni,nombre from empleados")

        # Recorrer cada fila y cargarlos en el tree
        for row in self.cursor.fetchall(): # fetchall(): recupera todas las filas del resulatado de la consulta
            self.tree.insert("",0,text=row[0],values=(row[1],row[2]))

    def insertar(self):
        nuevo_empleado = (self.txt_dni.get(),self.txt_nombre.get()) # tupla a partir de datos de las cajas de texto
        query = "insert into empleados(dni,nombre) values(%s,%s)" # consulta SQL # %s: marcadores de posicion
        self.cursor.execute(query,nuevo_empleado) 
        self.db.commit() # Confirma los cambios en la base de datos
        self.cargar_empleados()
    

        