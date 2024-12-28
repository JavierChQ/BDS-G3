# Insertar datos
file_write = open('alumnos.txt','w') # w: escribe la ultima linea de comando
file_write.write('100,ana,ana@gmail.com')
file_write.close()

file_write = open('alumnos.txt','a') # a: agrega datos
file_write.write('\n') # \n: slto de linea
file_write.write('200,pepe,pepe@gmail.com')
file_write.close()

# Leer datos
file_read =open('alumnos.txt','r')
alumnos = file_read.read()
print(alumnos)
print(type(alumnos))
file_read.close()