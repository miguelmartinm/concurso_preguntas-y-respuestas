from categoria import *
from opciones import *

import random

class Pregunta:
    
    def __init__(self, nivel):
        self.pregunta = {}
        self.opciones_ = None
        self.categorias = Categoria().obtener_list_ordenada_categorias()
        self.nivel = nivel
        self.lista_preguntas_del_nivel = []
        self.enunciado_pregunta = ""
        

    def obtener_pregunta_del_nivel(self, nivel):
        """ Obtiene de Categoria() las preguntas con el mismo nivel.
            Retorna: un diccionario con la pregunta elegida al azar del nivel."""
        
        # lista_preguntas_del_nivel recibe una lista ordenada de las categorías del nivel
        self.lista_preguntas_del_nivel = self.categorias[nivel-1]

        # Seleccion aleatoria del indice de la lista_preguntas_del_nivel
        pos_aleatoria = random.randint( 0, len(self.lista_preguntas_del_nivel) -1  )

        # Asigna al dic pregunta la pregunta seleccionada al azar de la categoría
        self.pregunta = self.lista_preguntas_del_nivel[pos_aleatoria]        

        return self.pregunta

        
    def enunciado_pregunta_(self):
        self.enunciado_pregunta = self.pregunta.get('pregunta') 
               
        return self.enunciado_pregunta        


    def mostrar_opciones(self):
        self.opciones_ = Opciones(self.pregunta) 

        return self.opciones_.obtener_opciones_de_pregunta()

                
# pregunta = Pregunta(1)
# #print(pregunta.categorias)
# print(pregunta.obtener_pregunta_del_nivel(5))
# print(pregunta.enunciado_pregunta_())

# print(pregunta.mostrar_opciones())


        





        

