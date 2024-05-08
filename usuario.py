# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-05-08
# RLAB-23-02-09-0044-2
#

# Desarrollo
class Usuario():
    def __init__(self, nombre:str, edad:str, correo:str, region:str) -> None:
        self.__nombre = nombre
        self.__edad = edad
        self.__correo = correo
        self.__region = region
    
    # getters
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    def get_correo(self):
        return self.__correo
    def get_region(self):
        return self.__region
    
    # setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_edad(self, edad):
        self.__edad = edad
    def set_correo(self, correo):
        self.__correo = correo
    def set_region(self, region):
        self.__region =  region

    def contestar_encuesta():
        pass