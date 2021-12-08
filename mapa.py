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
        """llena la lista de posiciones para llegar a una nueva celda, solo funciona si se mueve hacia adelante"""
        posicion_actual= self.personaje_seleccionado_ahora_mismo.get_pos()
        if posx < posicion_actual[1] and posy== posicion_actual[0]:# X atras
            for x in range(posicion_actual[1]-posx):
                nueva_X_atras=(posicion_actual[1]-1-x)
                nueva_posicion_moviendoteX_atras=nueva_X_atras,posy
                self.posiciones.append(nueva_posicion_moviendoteX_atras)
                

                

        if posx > posicion_actual[1] and posy== posicion_actual[0]:# X adelante
            for x in range(posx-posicion_actual[1]):
                nueva_X_adelante=(posicion_actual[1]+1+x)
                nueva_posicion_moviendoteX_adelante=nueva_X_adelante,posy
                self.posiciones.append(nueva_posicion_moviendoteX_adelante)
                
        if posy > posicion_actual[0] and  posx== posicion_actual[1]:# Y adelante
            for y in range(posy-posicion_actual[0]):
                nueva_Y_adelante=posicion_actual[0]+1+y
                nueva_posicion_moviendoteY_adelante=(posicion_actual[1],nueva_Y_adelante)
                self.posiciones.append(nueva_posicion_moviendoteY_adelante)
        
        if posy < posicion_actual[0] and  posx== posicion_actual[1]:# Y atras
            for y in range(posicion_actual[0]-posy):
                nueva_Y_atras=posicion_actual[0]-1-y
                nueva_posicion_moviendoteY_atras=(posicion_actual[1],nueva_Y_atras)
                self.posiciones.append(nueva_posicion_moviendoteY_atras)
                
        if posx != posicion_actual[1] or posy !=posicion_actual[0]:
            teletransportacion= posx,posy
            self.posiciones.append(teletransportacion)

        

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
        