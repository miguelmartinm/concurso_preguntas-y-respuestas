#from jugador import Jugador
from pregunta import *

class Ronda:

    def __init__(self):
        self.nivel = 0
        self.puntos_ronda = 0
        self.pregunta_ronda = None

    def crear_ronda(self):
        self.pregunta_ronda = Pregunta(self.nivel)
        print('\n')
        
        for ronda in range(5):
            print('*'*30)
            print(f'            Ronda {ronda+1}')
            print('*'*30)
            pregunta = self.pregunta_ronda.obtener_pregunta_del_nivel(ronda+1)
            enunciado = self.pregunta_ronda.enunciado_pregunta_()
            opciones = self.pregunta_ronda.mostrar_opciones()


            print(f"Categoría: {pregunta['categoria']}" )
            print(f"Pregunta: {enunciado} ")
            print(f" \
                    \na. {opciones[0]}  \
                    \nb. {opciones[1]}  \
                    \nc. {opciones[2]}  \
                    \nd. {opciones[3]}  \
            \n\n")

            #print(f"Pregunta: '{pregunta['pregunta']}" )





        

      