from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import mysql.connector

class EmpresaTk:
    
    def __init__(self,app):
        self.app = app
        self.app.title('Empresas')
        self.app.geometry('640x480')
        
        self.db = mysql.connector.connect(
                host='localhost',
                user='root',
                password='mysqljavier',
                database='datag3')
        
        self.cursor = self.db.cursor()
        
        frame = LabelFrame(self.app, text='Registrar nueva Empresa')
        frame.grid(row=0, column=0, columnspan=2, pady=10,padx=50)
        
        lb_ruc = Label(frame, text='RUC')
        lb_ruc.grid(row=1, column=0)
        self.txt_ruc = Entry(frame)
        self.txt_ruc.grid(row=1, column=1)
        
        lb_razon_social = Label(frame, text='RAZON SOCIAL')
        lb_razon_social.grid(row=2, column=0)
        self.txt_razon_social = Entry(frame)
        self.txt_razon_social.grid(row=2, column=1)
        
        btn_insertar = Button(frame, text='Insertar',command=self.insertar)
        btn_insertar.grid(row=3, columnspan=2, sticky=W+E)
        
        #grilla de empresas
        self.tree = Treeview(self.app, columns=('RUC','RAZON SOCIAL'))
        self.tree.grid(row=4, column=0, columnspan=2,padx=10,pady=10)
        self.tree.heading('#0', text='ID')
        self.tree.heading('RUC', text='RUC')
        self.tree.heading('RAZON SOCIAL', text='RAZON SOCIAL')
        
        self.cargar_empresas()
        
    def cargar_empresas(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        self.cursor.execute("select id,ruc,razon_social from empresa order by id")
        for row in self.cursor.fetchall():
            self.tree.insert('',0,text=row[0],values=(row[1],row[2]))
            
    def insertar(self):
        nueva_empresa = (
            self.txt_ruc.get(),
            self.txt_razon_social.get()
        )
        
        query = "insert into empresa(ruc,razon_social) values(%s,%s)"
        self.cursor.execute(query,nueva_empresa)
        self.db.commit()
        self.cargar_empresas()
        
        
app = Tk()
app_empresa = EmpresaTk(app)
app.mainloop()