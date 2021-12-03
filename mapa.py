from random import randint
import numpy as np
from aldeano import Aldeano
from celda import Celda
from fundador import Fundador
from guerrero import Guerrero
from montaña import Montaña
from aldeano import Aldeano
from tierra import Tierra
from water import Agua
from personaje import Personaje



class Mapa():
    #es el modelo
    def __init__(self, celdastotaleXPantalla = 40, celdastotalesYPantalla = 20 ,cantidadFilas = 100, cantidadColumnas = 100):
        self.centroPantallaY = cantidadFilas // 2 # Se divide para obtener el centro de la matriz, que es 100x100 
        self.centroPantallaX = cantidadColumnas // 2
        self.maximo_minimo_pantalla()
        self.mapa = self.generarMapa(cantidadFilas, cantidadColumnas, False) #Le asigno un valor a cada posicion 
        self.personaje = self.crear_personaje(Aldeano,celdastotaleXPantalla,celdastotalesYPantalla)
        self.fundador= self.crear_personaje(Fundador,celdastotaleXPantalla,celdastotalesYPantalla)
        self.guerrero=self.crear_personaje(Guerrero,celdastotaleXPantalla,celdastotalesYPantalla)
        self.personaje_seleccionado_ahora_mismo = self.personaje
        self.posiciones=[]
        
        

    def crear_personaje(self,personaje, celdas_totales_pantallax, celdas_totales_pantallay):
         spawn = self.playerSpawn(celdas_totales_pantallax,celdas_totales_pantallay) #aparece en el centro de una celda
         objeto_personaje= personaje(spawn) #al objeto personaje se le pasa la posicion de spawn
         #self.get_mapa().set_personaje(objeto_personaje)
         self.mapa[spawn[0]][spawn[1]].set_personaje(objeto_personaje)#setea al objeto personaje en una celda predeterminada
         print(objeto_personaje.get_pos())
         return objeto_personaje

    def llenar_lista(self,posx,posy):
        mas_uno=1
        
        posicion_actualY,posicion_actualX= self.personaje_seleccionado_ahora_mismo.get_pos()
        if posx != posicion_actualX and posy== posicion_actualY:
            for x in range(posicion_actualX-posx):
                nueva_X=mas_uno+posicion_actualX
                nueva_posicion=nueva_X+1,posy
                self.posiciones.append(nueva_posicion)
            print(self.posiciones)

                
        if posy != posicion_actualY and  posx== posicion_actualX:
            for y in range(posicion_actualY-posy):
                nueva_Y=posicion_actualY+mas_uno
                nueva_posicion=posx+1,nueva_Y
                print(nueva_posicion)
                self.posiciones.append(nueva_posicion)
            print(self.posiciones)

    def maximo_minimo_pantalla(self):

        """Establezco los limites para no pasarme a la hora de mover la camara"""
        self.maxPositivaY = 90
        self.minNegativoY = 10

        self.maxPositivaX = 80
        self.minNegativoX = 20
    

    def generarMapa(self, fil, col, val):
        """SE crea el mapa con la amtriz y se le agrega si es montaña, agua o tierra"""
        mapa = []
        tipos = [Montaña, Agua, Tierra]
        for i in range(fil):
            mapa.append([])
            for j in range(col):
                num = randint(0,100)
                if num<5:
                    tipo = tipos[0]
                elif num>98:
                    tipo = tipos[1]
                else:
                    tipo = tipos[2]

                mapa[i].append(tipo())
        return mapa
            

    def get_mapa(self):
        """devuelve el mapa creado"""
        return self.mapa


    def playerSpawn(self, celdasPantallaTotalHorizontal, celdasPantallaTotalVertical):
        """Se genera el spawn del personaje aleatoriamente en el centro de la pantalla"""
        yMinimaPantalla = ((self.centroPantallaY - 10) + (celdasPantallaTotalVertical // 2)) + 2
        yMaximaPantalla = ((self.centroPantallaY - 10) + (celdasPantallaTotalVertical // 2)) - 2
                            
        
        xMinimaPantalla =  ((self.centroPantallaX - 20) + (celdasPantallaTotalHorizontal // 2)) + 2
        xMaximoPantalla =  ((self.centroPantallaX - 20) + (celdasPantallaTotalHorizontal // 2)) - 2

        numX = randint(xMaximoPantalla , xMinimaPantalla)
        numY = randint(yMaximaPantalla, yMinimaPantalla)
        while self.mapa[numY][numX].isSpawnable() != True or self.mapa[numY][numX].isSpawnableRecurso() != True:
            numX = randint(xMaximoPantalla , xMinimaPantalla)
            numY = randint(yMaximaPantalla, yMinimaPantalla) 
        
            
        self.descubirMapa(numY, numX, 4)
        return numY, numX


    def getCentroPantalla(self):
        return self.centroPantallaX, self.centroPantallaY
        

    

    def descubirMapa(self, posPersonajeY, posPersonajeX, visibilidad):
        """Se descubre el mapa a medida que el personaje avanza"""
        for y in range((posPersonajeY + visibilidad), (posPersonajeY - visibilidad)):
            for x in range((posPersonajeX + visibilidad), (posPersonajeX - visibilidad)):
                if 0 < y < self.fila:
                    if 0 < x < self.col:
                        self.mapa[y][x].visibilizar()
   
    
    def get_item(self, y, x):
        """devuelve lo que haya en una celda especifica"""
        return self.mapa[y][x]

    def get_personaje(self):
        """Devuelve al personaje que tiene la clase mapa"""
        return self.personaje
    
    
    

    def set_centro_pantalla_y(self, numeroNuevoY):
        """Se setea el nuevo centro de la pantalla en el eje Y"""
        self.centroPantallaY =  self.centroPantallaY + numeroNuevoY
        if self.centroPantallaY <= self.minNegativoY:
            self.centroPantallaY = self.minNegativoY
        if self.centroPantallaY >= self.maxPositivaY:
            self.centroPantallaY = self.maxPositivaY
            
    def set_centro_pantalla_x(self, numeroNuevoX):
        """Se setea el nuevo centro de la pantalla en el eje X"""
        self.centroPantallaX = self.centroPantallaX + numeroNuevoX
        if self.centroPantallaX <= self.minNegativoX:
            self.centroPantallaX = self.minNegativoX
        if self.centroPantallaX >= self.maxPositivaX:
            self.centroPantallaX = self.maxPositivaX 
        