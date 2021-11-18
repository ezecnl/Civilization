import pygame

class Personaje:
    def __init__(self, posicion):
        self.estado = True
        self.vida = None
        self.velocidad = None
        self.celdas_visibles = 4
        self.comida = None
        self.url_imagen = "Tropas y personajes/GraveRobber.png"
        self._sprite = None
        self.posX = posicion[1]
        self.posY = posicion[0]
    
    def set_sprite(self, sprite):
        """Seteo el sprite"""
        self._sprite = sprite

    def get_url_imagen(self):
        """Obtengo la url de la imagen que voy a cargar y la devuelo"""
        return self.url_imagen

    def get_sprite(self):
        """devuelvo el sprite"""
        return self._sprite

    def get_pos(self):
        return self.posY, self.posX
    
    def mover_personaje(self, posicionNueva,mapa):
        """Cargo la nueva posicion para luego moverme por el mapa"""
        elmapa=mapa.get_mapa()
        laceldaanterior=elmapa[self.posY][self.posX]
        laceldaanterior.eliminar_personaje()
        self.posY = posicionNueva[1]
        self.posX = posicionNueva[0]
        laceldanueva=elmapa[self.posY][self.posX]
        laceldanueva.set_personaje(self)
        