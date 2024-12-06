# bucle for

tabla = input("ingrese la tabla de multiplicar: ")

for contador in range(1,13):
    print(f"{tabla} x {contador} = {int(tabla)*int(contador)}")