from banco_preguntas import Banco_preguntas
from jugador import Jugador
from ronda import *


    
def menu():
    print('\nCONCURSO | PREGUNTAS Y RESPUESTAS |')
    print('*'*50)
    print('1-> |- Iniciar juego')
    print('2-> |- Instrucciones')
    print('3-> |- Puntuaciones')    
    print('4-> |- Cargar preguntas desde archivo csv')
    print('5-> |- Salir')   
    

if __name__ == '__main__':   

    menu()    
    opcion = int(input('\nOpción -> '))

    if opcion == 1:
        jugador = Jugador('')
        jugador.nombre = ''

        ronda = Ronda()
        ronda.crear_ronda()



