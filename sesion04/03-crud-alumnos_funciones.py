import os
from time import sleep
from matriculas.lib_alumnos import *

opcion = 0

while(opcion < 5):
    os.system("cls")
    menu()
    opcion = int(input("INGRESE OPCION : "))
    os.system("cls")

    if opcion == 1:
        registrar()
    elif opcion == 2:
        mostrar()
    elif opcion == 3:
        actualizar()
    elif opcion == 4:
        eliminar()
    elif opcion == 5:
        mostrar_mensaje("[5] SALIR")
    else:
        mostrar_mensaje("OPCCION INVALIDA!!!")

    sleep(1)