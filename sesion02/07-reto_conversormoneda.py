# conversor de monedas

print("\n===== Conversor de monedas========\n")

tipo_cambio=float(input("Ingrese el tipo de cambio: 1 dolar = S/ "))
bandera ="si"
while(bandera == "si"):
    operacion = input("""Seleccione una opcion:
                    1) Convertir de soles a dolares
                    2) Convertir de dolares a soles
                    3) salir
                    """)
    
    if(operacion == "1"):
        monto = float(input("Ingrese el monto a convertir: "))
        resultado = monto / tipo_cambio
        print(f"S/ {monto} equivale a $ {resultado}")

    elif(operacion == "2"):
        monto = float(input("Ingrese el monto a convertir: "))
        resultado = monto * tipo_cambio
        print(f"$ {monto} equivale a S/ {resultado}")
    
    elif(operacion == "3"):
        print("Hasta luego")
        exit()

    else:

        print("Opcion no valida")

    bandera = input("Desea realizar otra operacion: (si | no) ")
    print("Hasta luego")