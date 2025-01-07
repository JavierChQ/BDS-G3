from tkinter import *
from lib_empleados import Empleados

app = Tk()

if __name__ == '__main__':
    empleados = Empleados(app)
    app.mainloop()