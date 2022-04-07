from banco_preguntas import *


class Categoria:
     
     def __init__(self):
         #self.nivel_dificultad = nivel_dificultad
         self.categorias = []   
         self.__banco_Preguntas = Banco_preguntas().cargar_preguntas_desde_csv()
     
     
     def crear_arreglos_en_categorias(self):
          """ Crea sublistas dentro de la lista categorias[]
               Retorna: lista de listas"""
          for nivel in range(5):
               self.categorias.append([])

          return self.categorias


     def obtener_list_ordenada_categorias(self):
          """ Ordena en la lista categorias[] las preguntas obtenidas de banco_preguntas.
              categorias = [ [{},{},{},{}] , ... , [{},{},{},{}] ]  donde cada posición 
              de la categorias es un nivel."""
          categorias = self.crear_arreglos_en_categorias()

          #
          for pregunta in self.__banco_Preguntas:
               categoria = pregunta['categoria']          
               
               if categoria == 'categoria':
                    pass
               else:
                    for i in range(5):
                         if int( categoria ) == i+1:                         
                              categorias[i].append(pregunta)
          
          return categorias
          #print(categorias)         

#categoria = Categoria(0) 
#print(categoria.ordenar_categorias())