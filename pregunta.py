# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-05-07
# RLAB-23-02-09-0044-2
#

# Librerias
from alternativa import Alternativa

# Desarrollo
class Pregunta():
    def __init__(self, enunciado:str, ayuda:str, requerido:bool, alternativas:str) -> None:
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerido = requerido
        self.alternativas = [Alternativa(dict["contenido"],dict["ayuda"]) for dict in alternativas]
        
    def mostrar_pregunta(self):
        print(self.enunciado)
        if self.ayuda:
            print('ayuda', self.ayuda)