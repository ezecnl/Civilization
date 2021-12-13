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
        self.fuente_terciaria=pygame.font.SysFont("Gill Sans", 20, bold=False, italic=False)
        self.limites_actualizados(limites)
        self.cargar_sprites()
        self.controlador = controlador
        self.click=pygame.mouse.get_pressed()
        
        

    
    def limites_actualizados(self,limites):
        """el rectangulo de celdas que se llega a ver"""
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
                estrutura= celda.get_estructura()
                if estrutura != None:
                    estrutura.set_sprite(self.cargar_foto(estrutura.get_url_imagen()))


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
                
                self.screen.blit(self.mapa.get_item(y,x).get_sprite(), (forX * self.tamañoFotoCelda, forY * self.tamañoFotoCelda))#entro en el objeto mapa, pido lo que haya en la celda,de lo que haya pido el sprite para despues blitearlo
                try:
                    self.screen.blit(self.mapa.get_item(y,x).get_recurso().get_sprite(), (forX * self.tamañoFotoCelda, forY * self.tamañoFotoCelda))
                except:
                    pass
                try:
                    self.screen.blit(self.mapa.get_item(y,x).get_personaje().get_sprite(), (forX * self.tamañoFotoCelda , forY  * self.tamañoFotoCelda))
                    
                except:
                   pass
                try:
                    self.screen.blit(self.mapa.get_item(y,x).get_estructura().get_sprite(),(forX * self.tamañoFotoCelda , forY  * self.tamañoFotoCelda))
                except:
                    pass         
                forX += 1

            forY += 1 
        
    
    def get_mouse_pos(self):
        return pygame.mouse.get_pos()

  

    
    
    def boton(self,posx,posy,ancho,altura,action=None,pantalla="none"):
        """Crea una zona en la pantalla que si recibe un click hace una accion"""
        mouse= self.get_mouse_pos()
        click = pygame.mouse.get_pressed()

        if posx+ancho > mouse[0] > posx and posy+altura > mouse[1] > posy: #si el mouse esta entre x,x+ancho e y,y+altura
            
            if click[0] == 1 != None: 
                if pantalla=="jugar":
                    self.controlador.empezar_juego()
                if pantalla=="reclutar":
                    self.controlador.no_mover_personaje()
                    self.controlador.mostrar_menu_personajes()
                if pantalla=="prejuego":
                    self.controlador.menu_mapa()
                if pantalla=="aldeano":
                    self.controlador.aldeano()#crea un aldeano
                if pantalla=="guerrero":
                    self.controlador.guerrero()#crea un guerrero
                if pantalla=="fundador":
                    self.controlador.fundador()#crea un fundador
                if pantalla=="cancelar_personajes":
                    self.controlador.ocultar_menu_personaje()
                    self.controlador.si_mover_personaje()
                if pantalla=="Casa":
                    self.controlador.casa_seleccionada()
                    
        
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

    def menu_personajes(self):
        fondo= pygame.image.load('Imagenes/Menu_personajes.png')
        self.screen.blit(fondo,(600,0))
        self.boton(631,59,162,44,action=self.click,pantalla="aldeano")
        self.boton(631,157,162,44,action=self.click,pantalla="guerrero")
        self.boton(631,251,162,44,action=self.click,pantalla="fundador")
        self.boton(655,336,106,29,action=self.click,pantalla="cancelar_personajes")

    def menu_en_juego(self):
         comida=self.mapa.personaje_seleccionado_ahora_mismo.inventario["Comida"]
         inventario_comida= self.fuente_terciaria.render(str(comida), True, (0,0,0))
         texto_comida= self.fuente_terciaria.render("Comida", True, (0,0,0))

         madera=self.mapa.personaje_seleccionado_ahora_mismo.inventario["Madera"]
         inventario_madera= self.fuente_terciaria.render(str(madera), True, (0,0,0))
         texto_madera= self.fuente_terciaria.render("Madera", True, (0,0,0))

         piedra=self.mapa.personaje_seleccionado_ahora_mismo.inventario["Piedra"]
         inventario_piedra= self.fuente_terciaria.render(str(piedra), True, (0,0,0))
         texto_piedra= self.fuente_terciaria.render("piedra", True, (0,0,0))

         hierro=self.mapa.personaje_seleccionado_ahora_mismo.inventario["Hierro"]
         inventario_hierro= self.fuente_terciaria.render(str(hierro), True, (0,0,0))
         texto_hierro= self.fuente_terciaria.render("Hierro", True, (0,0,0))

         reclutar= pygame.image.load('Imagenes/boton_reclutar.png')

         self.screen.blit(inventario_comida,(75,0))
         self.screen.blit(texto_comida,(10,0))

         self.screen.blit(inventario_madera,(175,0))
         self.screen.blit(texto_madera,(110,0))

         self.screen.blit(inventario_piedra,(275,0))
         self.screen.blit(texto_piedra,(210,0))

         self.screen.blit(inventario_hierro,(375,0))
         self.screen.blit(texto_hierro,(310,0))

         self.screen.blit(reclutar,(20,350))
         self.boton(20,350,30,30,action=self.click,pantalla="reclutar")

         self.boton(0,0,100,50,action=self.click,pantalla="Casa")
         
        
        


            
