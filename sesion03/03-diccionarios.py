capitales ={
    'Perú':'Lima',
    'Ecuador':'Quito',
    'Chile':'Santiago'
}

pais = input('Ingrese el pais: ')
if pais in capitales:
    capital = capitales.get(pais)
    print(f'La capital de {pais} es {capital}')
    eliminar_capital = input('Desea eliminar la capital?( si | no)')
    if eliminar_capital == 'si':
        capitales.pop(pais,'No existe')
        print(capitales)
else:
    print(f'No se encontró la capiatl de {pais}')
    nueva_capital = input(f'ingresa capital de {pais}: ')
    capitales.update({pais:nueva_capital})
    print(capitales)