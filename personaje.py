import pygame
import time

class Personaje:
    def __init__(self, posicion):
        self.estado = True
        self.vida = None
        self.velocidad = None
        self.celdas_visibles = 4
        self.comida = None
        self.url_imagen = None
        self._sprite = None
        self.posX = posicion[1]
        self.posY = posicion[0]
        self.posiciones_futuras = []
        self.inventario = {"Comida": 0,"Madera":0,"Piedra":0,"Hierro":0 }


    def consumir_recurso(self,recurso):
        pass

    def agregar_inventario(self,material,cantidad):
        """suma al inventario el material que se haya minado"""
        self.inventario[material] += cantidad 

    def eliminar_del_inventario(self,material,cantidad):
        """se le resta al inventario lo que se haya usado"""
        self.inventario[material] -= cantidad

    def aplicar_costo(self,objeto):
        costos= objeto.costo
        for tipo,cantidad in costos.items():
            self.eliminar_del_inventario(tipo,cantidad)

    def puedo_contruir(self,estructura):
        construccion= True
        for tipo,costo in estructura.costo.items():
            if costo > self.inventario[tipo]:
                construccion=False
        return construccion

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

    def mover(self, mapa):
        if len(self.posiciones_futuras) > 0:
            if self._mover(self.posiciones_futuras[0], mapa):
                self.posiciones_futuras.pop(0)

    def _mover(self, posicionNueva, mapa):
        """Elimino al personaje de su celda anterior para moverlo a la nueva"""
        if not mapa.get_item(posicionNueva[1],posicionNueva[0]).hayRecurso(): 
            elmapa=mapa.get_mapa()
            laceldaanterior=elmapa
            laceldaanterior.eliminar_personaje()
            self.posY = posicionNueva[1]
            self.posX = posicionNueva[0]

            laceldanueva=elmapa[self.posY][self.posX]
            laceldanueva.set_personaje(self)
            return True

        else:
            recurso = mapa.get_item(posicionNueva[1],posicionNueva[0]).get_recurso()
            self.consumir_recurso(recurso)
    
    
    def set_posiciones_futuras(self, lista_posiciones):
        self.posiciones_futuras=lista_posiciones
        
        
        