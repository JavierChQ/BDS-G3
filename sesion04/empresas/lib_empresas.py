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

        self.empresa_id = 0

        # INTERFAZ
        # Ventana principal      
        frame = LabelFrame(self.app, text="Registro de Empresas")
        frame.grid(row=0, column=0, columnspan=2, pady=10,padx=10)
        
        # Formulario
        lb_ruc = Label(frame, text="RUC")
        lb_ruc.grid(row=0, column=0)
        
        self.txt_ruc = Entry(frame)
        self.txt_ruc.grid(row=0, column=1)

        lb_razon_social = Label(frame, text="Razón Social")
        lb_razon_social.grid(row=0, column=2)
        
        self.txt_razon_social = Entry(frame)
        self.txt_razon_social.grid(row=0, column=3)
        
        # Botones
        self.btn_insertar = Button(frame,text="Insertar Nueva Empresa", command=self.insertar)
        self.btn_insertar.grid(row=0, column=4)
        
        self.btn_editar = Button(self.app,text="Editar Empresa",command=self.editar)
        self.btn_editar.grid(row=3, column=0)
        
        self.btn_eliminar = Button(self.app,text="Eliminar Empresa",command=self.eliminar)
        self.btn_eliminar.grid(row=3, column=1)
        
        # tabla
        self.tree = Treeview(self.app, columns=("RUC","Razón Social"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("RUC", text="RUC")   
        self.tree.heading("Razón Social", text="Razón Social")
        
        self.tree.grid(row=1, column=0,padx=20,pady=10,columnspan=2)

        self.cargar_empresas()

    # METODOS

    def cargar_empresas(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        self.cursor.execute("select id,ruc,razon_social from empresa")
        for row in self.cursor.fetchall():
            self.tree.insert("",0,text=row[0],values=(row[1],row[2]))
        
    def insertar(self):
        if self.empresa_id > 0:
            self.actualizar()
            return
        
        
        if not self.txt_ruc.get() or not self.txt_razon_social.get():
            messagebox.showwarning("Atención","Complete los campos")
            return
        
        nueva_empresa = (self.txt_ruc.get(),self.txt_razon_social.get())
        
        query = "insert into empresa(ruc,razon_social) values(%s,%s)"
        self.cursor.execute(query,nueva_empresa)
        self.db.commit()
        self.cargar_empresas()

    def editar(self):
        pass
    def eliminar(self):
        pass