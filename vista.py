import pygame
from sys import exit

from random import randint
import numpy as np
from pygame import surface
from pygame import transform
from pygame.constants import MOUSEBUTTONDOWN




class Vista:
    def __init__(self, controlador, mapa_actual, celdasPantallaTotalHorizontal, celdasPantallaTotalVertical, tamanioFotoCelda, anchoLargoPantalla,limites) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((anchoLargoPantalla[0],anchoLargoPantalla[1]))
        pygame.display.set_caption('Civilization')
        self.tamañoFotoCelda = tamanioFotoCelda # en pixeles
        self.celdasPantallaTotalHorizontal = celdasPantallaTotalHorizontal #40 celdas que entran horizontal en la pantalla
        self.celdasPantallaTotalVertical = celdasPantallaTotalVertical #20 celdas que entran vertical en la pantalla
        self.mapa = mapa_actual
        self.fuente= pygame.font.SysFont("Gill Sans",60, bold=True, italic=False)
        self.fuente_secundaria=  pygame.font.SysFont("Gill Sans", 30, bold=False, italic=False)
        self.limites_actualizados(limites)
        self.cargar_sprites()
        self.controlador = controlador
        self.click=pygame.mouse.get_pressed()
        
        

    
    def limites_actualizados(self,limites):
        self.anchoMinimo= limites[0]
        self.anchoMaximo= limites[1]
        self.largoMinimo= limites[2]
        self.largoMaximo= limites[3]


    def cargar_sprites(self):
        """Se cargan todos los sprites"""
        for fila in self.mapa.get_mapa():
            for celda in fila:
                celda.set_sprite(self.cargar_foto(celda.get_url_imagen()))#setea la imagen escalada
                recurso = celda.get_recurso()
                if recurso != None:
                    recurso.set_sprite(self.cargar_foto(recurso.get_url_imagen()))
                personaje = celda.get_personaje()
                if personaje != None:
                    personaje.set_sprite(self.cargar_foto(personaje.get_url_imagen()))


    def cargar_foto(self, imagen):
        """Cargo todas las fotos y las escalo al tamaño de las celdas de la matriz"""
        fotoOriginal = pygame.image.load(imagen)
        fotoEscalada = pygame.transform.scale(fotoOriginal, (self.tamañoFotoCelda + 2, self.tamañoFotoCelda + 2))
        return (fotoEscalada)
    



          

    def mostrar_mapa(self):
        """Dibujo el mapa con todos los sprites juntos"""  
        forY = 0
        
        for y in range(self.anchoMinimo, self.anchoMaximo):
            forX = 0
            for x in range(self.largoMinimo, self.largoMaximo):
                
                self.screen.blit(self.mapa.get_item(y,x).get_sprite(), (forX * self.tamañoFotoCelda, forY * self.tamañoFotoCelda))
                try:
                    self.screen.blit(self.mapa.get_item(y,x).get_recurso().get_sprite(), (forX * self.tamañoFotoCelda, forY * self.tamañoFotoCelda))
                except:
                    pass
                try:
                    self.screen.blit(self.mapa.get_item(y,x).get_personaje().get_sprite(), (forX * self.tamañoFotoCelda , forY  * self.tamañoFotoCelda))
                    
                except:
                   pass

                forX += 1

            forY += 1 
        
    
    def get_mouse_pos(self):
        return pygame.mouse.get_pos()

    def dibujar_personaje(self,posX,posY):

        self.screen.blit(self.mapa.get_personaje().get_sprite(),(posX,posY))

    
    
    def boton(self,posx,posy,ancho,altura,action=None,pantalla="none"):
        """Crea una zona en la pantalla que si recibe un click hace una accion"""
        mouse= self.get_mouse_pos()
        click = pygame.mouse.get_pressed()

        if posx+ancho > mouse[0] > posx and posy+altura > mouse[1] > posy:
            
            if click[0] == 1 != None: 
                if pantalla=="jugar":
                    self.controlador.empezar_juego()
                if pantalla=="como_jugar":
                    pass
                if pantalla=="prejuego":
                    self.controlador.menu_mapa()
                    
        
    def menu_principal(self):
        
       
       azul=(0,0,200)
       fondo= pygame.image.load('Imagenes/fondoPrincipal.jpg')
       boton_rectangular= pygame.image.load('Imagenes/boton_rectangular.png')
       boton_rectangular_escalado= transform.scale(boton_rectangular,(230,50))
       fondo_escalado= transform.scale(fondo,(800,400))
       #boton_jugar= (280,150,215,35)
       #boton_como= (280,250,215,35)
       texto_titulo= self.fuente.render("CIVILIZATION", True, azul)
       texto_jugar= self.fuente_secundaria.render("jugar", True, azul)
       texto_ayuda= self.fuente_secundaria.render("como se juega",True,azul)

       self.screen.blit(fondo_escalado,(0,0)) 
       #pygame.draw.rect(self.screen,(255,255,255), boton_jugar)
       #pygame.draw.rect(self.screen,(255,255,255), boton_como) 
       self.screen.blit(boton_rectangular_escalado,(270,145))
       self.screen.blit(boton_rectangular_escalado,(270,245))
       self.screen.blit( texto_titulo,(200,10))
       self.screen.blit(texto_jugar,(350,150))
       self.screen.blit(texto_ayuda,(300,250))
       self.boton(280,150,215,35,action=self.click, pantalla="prejuego")
       self.boton(280,250,215,35,action=self.click, pantalla="como_jugar")

       

    def menu_mapa(self):
        fondo_boton=pygame.image.load('Imagenes/fondo_mapa.jpg')
        mapa_aleatorio= pygame.image.load('Imagenes/boton_mapa_aleatorio.png')
        mapa1=pygame.image.load('Imagenes/mapa1_boton.jpg')
        mapa2= pygame.image.load('Imagenes/mapa2_boton.jpg')
       
        mapa_aleatorio_escalado= transform.scale(mapa_aleatorio,(200,300))
        mapa1_escalado= transform.scale(mapa1,(200,300))
        mapa2_escalado= transform.scale(mapa2,(200,300))
        fondo_escalado= transform.scale(fondo_boton,(800,400))

        
        self.screen.blit(fondo_escalado,(0,0))
        self.boton(50,50,200,300,action=self.click, pantalla="jugar")
        self.screen.blit(mapa_aleatorio_escalado,(50,50))
        self.screen.blit(mapa1_escalado,(300,50))
        self.screen.blit(mapa2_escalado,(550,50))
        
        


            
