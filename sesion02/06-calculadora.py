# calculadora

bandera ="si"

while(bandera == "si"):
    print("calculadora con python")
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    operacion = int(input("""Que operacion desea hacer:
                        1) suma
                        2) resta
                        3) multiplicacion
                        4) division
                        """))
    if(operacion == 1):
        resultado = numero1 + numero2
        print(f'la suma de {numero1} + {numero2} es:  {resultado}')
    elif(operacion == 2):
        resultado = numero1 - numero2
        print(f'la resta de {numero1} - {numero2} es:  {resultado}')
    elif(operacion == 3):
        resultado = numero1 * numero2
        print(f'El producto de {numero1} * {numero2} es:  {resultado}')
    elif(operacion == 4):
        resultado = numero1 / numero2
        print(f'La division de {numero1} / {numero2} es:  {resultado}')
    else:
        print('La operacion no existe')

    bandera = input("Continuar? (si | no): ")