import csv
import os

preguntas = []
ARCHIVO_CSV = "banco_preguntas.csv"
CAMPOS_PREGUNTAS = ['categoria','pregunta','respuesta','opcion_a','opcion_b','opcion_c','opcion_d']

class Banco_preguntas:

    def __init__(self):
        self.__ARCHIVO_CSV = ARCHIVO_CSV
        self.__CAMPOS_PREGUNTAS = CAMPOS_PREGUNTAS
        self.__preguntas = preguntas

    def cargar_preguntas_desde_csv(self):
        """Obtiene las pregunta de un archivo csv ubicado en la misma carpeta donde
            se encuentre los archivos de clases del código. Si no lo encuentra, se
            captura el error. 
            Retorna: lista de diccionarios"""
        try:
            with open(self.__ARCHIVO_CSV, mode='r') as archivo:

                # Crea un objeto el cuál mapea la información leída a un diccionario cuyas llaves están dadas por el parámetro fieldnames
                reader = csv.DictReader(archivo, fieldnames = self.__CAMPOS_PREGUNTAS)                

                # Recorre el diccionario y lo agrega a __preguntas que contiene una lista de diccionarios
                for row in reader:
                    self.__preguntas.append(row)

                return self.__preguntas

        except FileNotFoundError:
            print('Archivo.csv no encontrado en la ruta especificada')    

    #@property
    # def preguntas(self):        
    #     return self.__preguntas