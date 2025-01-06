from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import mysql.connector

# Clases
class PacientesTK:
    # Metodo constructor
    def __init__(self,app):
        self.app = app
        self.app.title('Pacientes')
        self.app.geometry('640x480')

        # Conexion a la base de datos
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'mysqljavier',
            database = 'datag3'
        )
        self.cursor = self.db.cursor()
        
        # INTERFAZ
        # Ventana
        frame = LabelFrame(self.app, text='Registrar nuevo paciente')
        frame.grid(row=0,column=0,columnspan=2,padx=10,pady=50)

        # formulario
        lb_nombre = Label(frame,text='NOMBRE')
        lb_nombre.grid(row=1,column=0)
        self.txt_nombre = Entry(frame)
        self.txt_nombre.grid(row=1,column=1)

        lb_email = Label(frame,text='EMAIL')
        lb_email.grid(row=2,column=0)
        self.txt_email = Entry(frame)
        self.txt_email.grid(row=2,column=1)



        btn_insertar = Button(frame,text='INSERTAR',command=self.insertar_paciente)
        btn_insertar.grid(row=3,columnspan=2,sticky=W+E)

        # Grilla de pacientes
        self.tree = Treeview(self.app,columns=('NOMBRE','EMAIL'))
        self.tree.grid(row=4,column=0,columnspan=2,padx=10,pady=10)
        self.tree.heading('#0',text='id')
        self.tree.heading('EMAIL',text='EMAIL')
        self.tree.heading('NOMBRE',text='NOMBRE')

        self.cargar_pacientes()

    # Metodos
    def cargar_pacientes(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        self.cursor.execute("select id,nombres,email from pacientes order by id")
        for row in self.cursor.fetchall():
            self.tree.insert('',0,text=row[0],values=(row[1],row[2]))

    def insertar_paciente(self):
        nuevo_paciente = (
            self.txt_nombre.get(),
            self.txt_email.get()
            
        )
        
        query = "insert into pacientes(nombres,email) values(%s,%s)"
        self.cursor.execute(query,nuevo_paciente)
        self.db.commit()
        self.cargar_pacientes()

# Objetos
app = Tk()
app_paciente = PacientesTK(app)
app.mainloop()