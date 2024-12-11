import os
from time import sleep

dic_empresas = {
    '12345678':{
        'razon_social':'ANSUR PERU',
        'direccion':'Calle cartagena 434'
    }
}
ANCHO = 50
opcion = 0
while(opcion < 5):
    os.system("cls")
    print("="*ANCHO)
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESA
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("cls")

    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "[1] REGISTRAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("RUC    :")
        razon_social = input("RAZON SOCIAL  :")
        direccion = input("DIRECCION    :")
        dic_nueva_empresa = {
            ruc : {
                   'razon_social':razon_social,
                   'direccion': direccion
                  }
        }
        dic_empresas.update(dic_nueva_empresa)
        print("Empresa registrado con exito")
    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "[2] MOSTRAR EMPRESAS")
        print("=" * ANCHO)
        for ruc,datos in dic_empresas.items():
            print(f"RUC : {ruc}")
            print(f"RAZON SOCIAL : {datos['razon_social']}")
            print(f"DIRECCION : {datos['direccion']}")
            print("*"*ANCHO)
        input("Presion ENTER para continuar...")
    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "[3] ACTUALIZAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("INGRESE RUC DE LA EMPRESA: ")
        if ruc in dic_empresas:
            print(f"EMPRESA A ACTUALIZAR:  {dic_empresas[ruc]['razon_social']}")
            nueva_razon_social = input('RAZON SOCIAL : ')
            nueva_direccion = input('DIRECCION :')
            dic_act_empresa = {
                ruc : {
                    'razon_social' : nueva_razon_social,
                    'direccion' : nueva_direccion
                }
            }
            dic_empresas.update(dic_act_empresa)
            print("Empresa actualizada con exito")
    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "[4] ELIMINAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese el RUC de la empresa: ")
        if ruc in dic_empresas:
            dic_empresas.pop(ruc)
            print("Empresa eliminada")
        else:
            print("No se encontro la empresa")
    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "[5] SALIR")
        print("=" * ANCHO)
        print("Hasta luego")
    else:
        print("=" * ANCHO)
        print(" " * 10 + "OPCIÓN INVÁLIDA!!!")
        print("=" * ANCHO)

    sleep(2)