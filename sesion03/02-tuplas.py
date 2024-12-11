# tuplas: igual a las listas pero inmutables

dias = ('lunes','martes','miercoles','jueves')
print(dias)
print(type(dias))

# para agregar datos convertimos la tupla en lista
dias =list(dias)
print(type(dias))
dias.append("viernes")
dias=tuple(dias)
print(type(dias))

# correr una lista

for dia in dias:
    print(dia)