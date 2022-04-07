#from categoria import *


class Opciones:

    def __init__(self, pregunta_asociada):
        self.pregunta_asociada = pregunta_asociada
        self.opciones = []
        # self.respuesta


    def obtener_opciones_de_pregunta(self):
        """ Obtiene las opciones de la pregunta seleccionada al azar
            Retorna: lista con las opciones """

        
        # chr() recobra un caracter a partir de su representación en ascii.
        for letra_ascii in range(97,101):
            opcion = f'opcion_{ chr(letra_ascii) }'

            # Obtiene del dic pregunta_asociada las opciones y las adjunta a la lista opciones[]
            self.opciones.append( self.pregunta_asociada.get(opcion) )
        
        return self.opciones
        

    def opciones_pregunta(self):
        pass