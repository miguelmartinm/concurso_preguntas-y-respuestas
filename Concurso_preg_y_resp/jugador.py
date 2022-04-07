class Jugador:
    
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__acumulado = 0
        self.__nivel_alcanzado = 0

    @property
    def nombre(self):
        return self.__nombre


    @nombre.setter
    def nombre(self, nombre):
        if nombre != None:
            self.__nombre = input('Nombre de jugador: ')
            print(self.__nombre)
        else:
            raise ValueError('\nNo se ha definido un Nombre de jugador')
#----------------------------------------------

    @property
    def acumulado(self):
        return self.__acumulado
    

    @acumulado.setter
    def acumulado(self, acumulado):
        self.__acumulado = acumulado
#----------------------------------------------

    @property
    def nivel_alcanzado(self):
        return self.__nivel_alcanzado
    
    
    @nivel_alcanzado.setter
    def nivel_alcanzado(self, nivel_alcanzado):
        self.nivel_alcanzado = nivel_alcanzado

