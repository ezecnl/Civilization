from math import radians
from random import randint, choice
from celda import Celda


class Piedra(Celda):
    def __init__(self, is_visible=False) -> None:
        super().__init__(is_visible=False)
        self.vida = 60
        self.cantidadHierroOtorgado = [10, 20, 5, 15, 30]
        self.cantidadPiedraOtorgada = [40, 25, 6, 35, 60]
        self.url_imagen = "imagenes/piedra3.png"

    def esPicable(self):
        return True

    def minado(self):
        material=["Hierro","Piedra"]
        aleatorio= choice(material)
        print(aleatorio)
        if aleatorio=="Hierro":
            hierro= self.cantidadHierroOtorgado[randint(0,4)]
            return aleatorio,hierro
        if aleatorio=="Piedra":
            piedra= self.cantidadPiedraOtorgada[randint(0,4)]
            return aleatorio,piedra
        
        

    
