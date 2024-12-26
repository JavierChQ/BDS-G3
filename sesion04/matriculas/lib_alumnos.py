ANCHO = 50
dic_alumnos = {}

def mostrar_mensaje(texto):
    print("=" * ANCHO)
    print(" " * 10 + texto)
    print("=" * ANCHO)

def menu():
    mostrar_mensaje("GESTIÓN DE ALUMNOS")
    print("""
         [1] REGISTRAR ALUMNO
         [2] MOSTRAR ALUMNOS
         [3] ACTUALIZAR ALUMNO
         [4] ELIMINAR ALUMNO
         [5] SALIR
          """)
    print("=" * ANCHO)

def registrar():
    mostrar_mensaje("[1] REGISTRAR ALUMNO")
    dni = input("DNI    :")
    nombre = input("NOMBRE  :")
    email = input("EMAIL    :")
    dic_nuevo_alumno = {
        dni : {
            'nombre':nombre,
            'email': email
            }
    }
    dic_alumnos.update(dic_nuevo_alumno)
    print("Alumno registrado con exito")

def mostrar():

    mostrar_mensaje("[2] MOSTRAR ALUMNOS")
    for dni,datos in dic_alumnos.items():
        print(f"DNI : {dni}")
        print(f"Nombre : {datos['nombre']}")
        print(f"EMAIL : {datos['email']}")
        print("*"*ANCHO)
    input("Presion ENTER para continuar...")
def actualizar():
    mostrar_mensaje("[3] ACTUALIZAR ALUMNO")
    dni = input("INGRESE DNI DEL ALUMNO A ACTUALIZAR: ")
    if dni in dic_alumnos:
        print(f"ALUMNO A ACTUALIZAR:  {dic_alumnos[dni]['nombre']}")
        nuevo_nombre = input('NOMBRE : ')
        nuevo_email = input('EMAIL :')
        dic_act_alumno = {
            dni : {
                'nombre' : nuevo_nombre,
                'email' : nuevo_email
            }
        }
        dic_alumnos.update(dic_act_alumno)
        print("Alumno actualizado con exito")

def eliminar():
    mostrar_mensaje("[4] ELIMINAR ALUMNO")
    dni = input("Ingrese el DNI del alumno: ")
    if dni in dic_alumnos:
        dic_alumnos.pop(dni)
        print("Alumno eliminado")
    else:
        print("No se encontro el alumno")

