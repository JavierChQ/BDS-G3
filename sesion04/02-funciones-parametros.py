# parametro args

def sumar_infinito(*args):
    resultado = 0
    for numero in args:
        resultado = resultado + numero
    return resultado

sumar1 = sumar_infinito(1,3,4)
print(sumar1)

# parametro kwargs

def calculadora(**kwargs):
    ope = kwargs.get('ope')
    n1 = kwargs.get('n1')
    n2 = kwargs.get('n2')

    if ope == 'suma':
        resultado = n1 + n2
        print(f'La {ope} de {n1} y {n2} es: {resultado}')
    elif ope == 'resta':
        resultado = n1 - n2
        print(f'La {ope} de {n1} y {n2} es: {resultado}')
    elif ope == 'multiplicacion':
        resultado = n1 * n2
        print(f'La {ope} de {n1} y {n2} es: {resultado}')
    elif ope == 'division':
        resultado = n1 / n2
        print(f'La {ope} de {n1} y {n2} es: {resultado}')
    else:
        print("La operacion no existe")

calculadora(n1=2,n2=1,ope='suma')
calculadora(n1=2,n2=1,ope='resta')
calculadora(n1=2,n2=1,ope='multiplicacion')
calculadora(n1=2,n2=1,ope='division')
calculadora(n1=2,n2=1,ope='divis')