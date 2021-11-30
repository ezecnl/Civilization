from celda import Celda
import pygame
from numpy import random
from random import randint
from arbol import Arbol
from arbusto import Arbusto

class Tierra(Celda):
    def __init__(self, is_visible=False) -> None:
        super().__init__(is_visible=False)
        self.recurso = None
        self.velocidad = 1
        self.url_imagen = "imagenes/tierra.png"
        self.set_arbol()
        self.set_arbusto()
        
    
    def tiempo(self):
        return self.velocidad

    def set_arbol(self):
        """Se setean los arboles con probabilidades"""
        
        num = randint(9,100)
        if num > 90:
            self.recurso = Arbol()
            return True
        else:
            return False

    def set_arbusto(self):
        """Se setean los arbustos con probabilidades"""
        
        num = randint(9,100)
        if num > 96:
            self.recurso = Arbusto()
            return True
        else:
            return False

    

    def get_recurso(self):
        return self.recurso

    def isSpawnable(self):
        return True
    
    def isSpawnableRecurso(self):
        if self.recurso == None:
            return True
        else:
            return False
