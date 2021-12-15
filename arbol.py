from random import randint
from celda import Celda
from madera import Madera

class Arbol(Celda):
    def __init__(self, is_visible=False) -> None:
        super().__init__(is_visible=False)
        self.cantidadMaderaOtorgada = [60, 20, 10, 30]
        self.url_imagen = "imagenes/arbol_nuevo.png"
        self.vida= 4

    

    def adquirir(self):
        """crea una cantidad de madera"""
        
        self.vida -= 1
        return Madera(10)
        

        
        
        

