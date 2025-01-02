class Automovil:
    # METODO CONSTRUCTOR
    def __init__(selft,aa,pl,col,mar):
        selft.color = aa
        selft.placa = pl
        selft.color = col
        selft.marca = mar

    # METODOS
    def encender(selft):
        print('encender ' + selft.marca)
    def avanzar(selft):
        print('avanzar ' + selft.marca)
    def acelerar(selft):
        print('acelerar ' + selft.marca)
    def frenar(selft):
        print('frenar ' + selft.marca)

# CREACION DE OBJETOS
vw = Automovil(1970,'CH-1234','rojo','Volkswagen')
vw.encender()
vw.avanzar()
vw.acelerar()
vw.frenar()

tico = Automovil(1999,'TI-4321','amarillo','Daewo')
tico.encender()
tico.avanzar()
tico.acelerar()
tico.frenar()