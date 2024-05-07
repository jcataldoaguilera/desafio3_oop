# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-05-07
# RLAB-23-02-09-0044-2
#

# Librerias
from pregunta import Pregunta

# Desarrollo
class Encuesta():
    def __init__(self, nombre:str, listado_preguntas=None, listado_respuestas=None) -> None:
        self.nombre = nombre
        self.listado_preguntas = []
        self.listado_respuestas = []
    
    def add_listado_preguntas(self, listado_preguntas):
        self.listado_preguntas.append(listado_preguntas)

    def add_listado_respuestas(self, listado_respuestas):
        self.listado_respuestas.append(listado_respuestas)


class EncuestaLimitadaPorEdad(Encuesta):
    def __init__(self, nombre, edad_minima:int, edad_maxima:int, listado_preguntas=None, listado_respuestas=None):
        super().__init__(nombre, listado_preguntas, listado_respuestas)
        self.__edad_minima = edad_minima
        self.__edad_maxima = edad_maxima
    
    def get_edad_minima(self):
        return self.__edad_minima
    
    def get_edad_maxima(self):
        return self.__edad_maxima
    
    def set_edad_minima(self, edad_minima):
        self.__edad_minima = edad_minima
    
    def set_edad_maxima(self, edad_maxima):
        self.__edad_maxima = edad_maxima

class EncuestaLimitadaPorRegion(Encuesta):
    def __init__(self, nombre, lista_regiones, listado_preguntas=None, listado_respuestas=None):
        super().__init__(nombre, listado_preguntas, listado_respuestas)
        self.__lista_regiones = lista_regiones
    
    def get_lista_regiones(self):
        return self.__lista_regiones
    
    def set_lista_regiones(self, lista_regiones):
        self.__lista_regiones = lista_regiones