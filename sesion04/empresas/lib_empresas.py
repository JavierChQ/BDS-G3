from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import mysql.connector

class Empresa:
    # METODO CONSTRUCTOR
    def __init__(self,app):
        self.app = app
        self.app.title("Gestión de Empresas")
        self.app.geometry("640x380")

        # CONEXION CON LA BASE DE DATOS
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'mysqljavier',
            database = 'db_proyecto_datag3'
        )

        self.cursor = self.db.cursor()

        # VENTANA PRINCIPAL       
        frame = LabelFrame(self.app, text="Registro de Empresas")
        frame.grid(row=0, column=0, columnspan=2, pady=10,padx=10)
        
        # FORMULARIO
        lb_ruc = Label(frame, text="RUC")
        lb_ruc.grid(row=0, column=0)
        
        self.txt_ruc = Entry(frame)
        self.txt_ruc.grid(row=0, column=1)

        lb_razon_social = Label(frame, text="Razón Social")
        lb_razon_social.grid(row=0, column=2)
        
        self.txt_razon_social = Entry(frame)
        self.txt_razon_social.grid(row=0, column=3)
        
        self.btn_insertar = Button(frame,text="Insertar Nueva Empresa", command=self.insertar)
        self.btn_insertar.grid(row=0, column=4)
        
        self.btn_editar = Button(self.app,text="Editar Empresa",command=self.editar)
        self.btn_editar.grid(row=3, column=0)
        
        self.btn_eliminar = Button(self.app,text="Eliminar Empresa",command=self.eliminar)
        self.btn_eliminar.grid(row=3, column=1)
        
        # TABLA
        self.tree = Treeview(self.app, columns=("RUC","Razón Social"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("RUC", text="RUC")   
        self.tree.heading("Razón Social", text="Razón Social")
        
        self.tree.grid(row=1, column=0,padx=20,pady=10,columnspan=2)

    # METODOS
    def insertar(self):
        pass
    def editar(self):
        pass
    def eliminar(self):
        pass