# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-05-07
# RLAB-23-02-09-0044-2
#

class Alternativa():
    def __init__(self,contenido:str, ayuda:str) -> None:
        self.contenido = contenido
        self.ayuda = ayuda
        
    def mostrar_alternativa(self):
        print (self.contenido)
        if self.ayuda:
            print('ayuda', self.ayuda)