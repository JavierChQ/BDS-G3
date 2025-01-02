class Usuario:
    # VARIABLES
    __email = 'javier@gmail.com'
    __password = 'javier123'
    # METODO CONSTRUCTOR
    def __init__(self):
        pass
    # METODOS
    def set_password(self,password):
        self.__password = password
    
    def login(self,email,password):
        if(self.__email == email and self.__password == password):
            print(f'Bienvenido {self.__email}')
        else:
            print('datos incorrectos')
            
print('LOGIN DE USUARIOS')
email = input('Ingrese Email :')
password = input('Ingrese Password : ')

# OBJETOS
usuario = Usuario()
usuario.set_password(password) # cambia el password
usuario.login(email,password)