from celda import Celda
import pygame


class Agua(Celda):
    def __init__(self,is_visible=False) -> None:
        super().__init__(is_visible=False)
        self.velocidad = 0
        self.url_imagen = "imagenes/agua.jpg"
    
    def isSpawnable(self):
        return False

    def tiempo(self):
        return self.velocidad