import pygame

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
        self.inventario = {"Comida": 0,"Madera":0,"Piedra":0,"Hierro":0 }

    def agregar_inventario(self,material,cantidad):
        """suma al inventario el material que se haya minado"""
        self.inventario[material] += cantidad 

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
        """Elimino al personaje de su celda anterior para moverlo a la nueva"""
        elmapa=mapa.get_mapa()
        laceldaanterior=elmapa[self.posY][self.posX]
        laceldaanterior.eliminar_personaje()
        self.posY = posicionNueva[1]
        self.posX = posicionNueva[0]

        laceldanueva=elmapa[self.posY][self.posX]
        laceldanueva.set_personaje(self)

        #lista=mapa.posiciones
        #total_de_celdas_recorridas= len(lista)

        #for posicion in range(total_de_celdas_recorridas):#va a mover al personaje la cantidad de coordenadas que haya en la lista
            #elmapa=mapa.get_mapa()
            #laceldaanterior=elmapa[self.posY][self.posX]
            #laceldaanterior.eliminar_personaje()
            #self.posY = posicionNueva[1]
            #self.posX = posicionNueva[0]

            #laceldanueva=elmapa[self.posY][self.posX]
            #laceldanueva.set_personaje(self)
        
        #lista=[]  #para limpiar la lista despues de llegar a la nueva celda

        
        
        
        