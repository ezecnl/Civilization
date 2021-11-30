from random import randint
from celda import Celda

class Arbol(Celda):
    def __init__(self, is_visible=False) -> None:
        super().__init__(is_visible=False)
        self.cantidadMaderaOtorgada = [60, 20, 10, 30]
        self.url_imagen = "imagenes/arbol_nuevo.png"

    

    def minado(self):
        """devuelve que elemento es y un numero aleatorio de la lista"""
        madera= self.cantidadMaderaOtorgada[randint(0, 3)]
        
        return "Madera",madera
        
        

