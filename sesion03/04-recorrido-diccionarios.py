capitales ={
    'Perú':'Lima',
    'Ecuador':'Quito',
    'Chile':'Santiago'
}

# recorrido por claves
print('='*40 + "Recorrido por claves")
for clave in capitales.keys():
    print(clave)

#recorrido por valores
print('='*40 + "Recorrido por valores")
for valor in capitales.values():
    print(valor)

#recorrido por clave,valor
print('='*40 + "Recorrido por clave,valor")
for clave,valor in capitales.items():
    print(f'La capital de {clave} es {valor}')