import pygame
import time
from aldeano import Aldeano
from guerrero import Guerrero
from vista import Vista
from mapa import Mapa

class Juego:
    # Es el controlador
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.tamanioFotoCelda = 20
        self.anchoLargoPantalla = [800, 400]
        self.celdasPantallaTotalHorizontal = self.anchoLargoPantalla[0] // self.tamanioFotoCelda #40 
        self.celdasPantallaTotalVertical = self.anchoLargoPantalla[1] // self.tamanioFotoCelda #20
        self.mapa = Mapa() # es el modelo
        self.vista = Vista(self,self.mapa,self.celdasPantallaTotalHorizontal, self.celdasPantallaTotalVertical, self.tamanioFotoCelda, self.anchoLargoPantalla, self.setear_pantalla())
        self.juego_empezo = False
        self.ir_mapas= False #menu principal
        #self.poder_minar=False #menu principal
        self.crear_aldeano= False #menu personajes
        self.crear_guerrero=False #menu personajes
        self.crear_fundador=False #menu personajes
        self.reclutar_personaje=False #menu personajes
        

        self.no_mover= False

        self.jugar()
    
    
    def si_mover_personaje(self):
        self.no_mover=False

    def no_mover_personaje(self):
        self.no_mover=True

    def fundador(self):
        self.crear_fundador = True
        self.crear_fundador=False
        


    def guerrero(self):
        self.crear_guerrero = True
        self.crear_guerrero=False

    def aldeano(self):
        self.mapa.crear_personaje(Aldeano,self.celdasPantallaTotalHorizontal,self.celdasPantallaTotalVertical)
        #print(self.mapa.get_personaje().get_pos())
        self.vista.mostrar_mapa()
        

    def ocultar_menu_personaje(self):
        self.reclutar_personaje=False
        

    def mostrar_menu_personajes(self):
        self.reclutar_personaje=True

    

    def empezar_juego(self):
        self.juego_empezo = True

    def menu_mapa(self):
        self.ir_mapas= True

    def jugar(self):
        while True: 
            if not self.juego_empezo:#para que los menus se queden en la pantalla
               self.vista.menu_mapa()
            else:
                self.vista.mostrar_mapa()
                self.vista.menu_en_juego()
                
                if self.reclutar_personaje==True:
                    self.vista.menu_personajes()

            if not self.ir_mapas:
                self.vista.menu_principal()
            
            if self.crear_aldeano==True:
                self.mapa.crear_personaje(Aldeano,self.mapa.celdastotaleXPantalla,self.mapa.celdastotalesYPantalla)#deberia crear un nuevo peronaja pero no anda
                pygame.display.update()
            if self.crear_guerrero==True:
                #self.mapa.guerrero
                self.mapa.crear_personaje(Guerrero,self.mapa.celdastotaleXPantalla,self.mapa.celdastotalesYPantalla)#no anda
                #self.vista.mostrar_mapa()
                
            if self.crear_fundador==True:#no anda
                self.mapa.fundador
                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    self.movimiento_pantalla(event.key)
                    self.vista.limites_actualizados(self.setear_pantalla())#setear nuevos llimites despues de mover la camara

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:#click derecho
                        if self.juego_empezo== True:#si ya se muestra el mapa
                            self.mapa.personaje_seleccionado_ahora_mismo=self.mapa.get_item(self.mouse_posicion()[1],self.mouse_posicion()[0]).get_personaje()#seleccion del personaje que voy a mover  
                            print(self.mapa.personaje_seleccionado_ahora_mismo)
                    elif event.button == 1: #click izquierdo

                        if self.no_mover== False:

                            
                            if self.mapa.get_item(self.mouse_posicion()[1],self.mouse_posicion()[0]).hayRecurso()==False:#no se puede spawnear en el agua
                                if self.mapa.get_item(self.mouse_posicion()[1],self.mouse_posicion()[0]).isSpawnable()==True:    
                                    if not self.mapa.get_item(self.mouse_posicion()[1],self.mouse_posicion()[0]).get_personaje():#si la celda no contiene un personaje te podes mover
                                        #self.mapa.get_personaje().mover_personaje(self.mouse_posicion(),self.mapa)
                                        self.mapa.llenar_lista(self.mouse_posicion()[0],self.mouse_posicion()[1])
                                        #self.mapa.personaje_seleccionado_ahora_mismo.mover_personaje(self.mouse_posicion(),self.mapa)
                                        #self.mapa.personaje_seleccionado_ahora_mismo.mover_personaje(self.mapa.posiciones,self.mapa)
                                        self.movimientos_por_celdas()
                                        #print(self.mouse_posicion()[0],self.mouse_posicion()[1])

                            if self.mapa.personaje_seleccionado_ahora_mismo.poder_picar()== True:
                                   
                                if self.mapa.get_item(self.mouse_posicion()[1],self.mouse_posicion()[0]).hayRecurso()==True:#sino se puede spawnear hay un recuro picable
                                    
                                    self.mapa.get_item(self.mouse_posicion()[1],self.mouse_posicion()[0]).minar(self.mapa.personaje_seleccionado_ahora_mismo)
                                    self.vista.mostrar_mapa()
            
            
                      
           

            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(60)#frames
        
    def movimientos_por_celdas(self):
        lista= self.mapa.posiciones
        total_de_celdas_recorridas= len(lista)
        
        for posicion in range (total_de_celdas_recorridas):

            self.mapa.personaje_seleccionado_ahora_mismo.mover_personaje(lista[posicion],self.mapa)             
            print("posicion",lista[posicion])        
            time.sleep(0.5)
            self.vista.mostrar_mapa() 
            pygame.display.update()
         
            
           
        
        self.mapa.posiciones=[]    
        

    def movimiento_pantalla(self, key):
        """Me muevo por la pantalla hasta los limites de la matriz"""
        if key == pygame.K_UP: 
            self.mapa.set_centro_pantalla_y(-2)
        if key == pygame.K_DOWN:
            self.mapa.set_centro_pantalla_y(2)
        if key == pygame.K_LEFT:
            self.mapa.set_centro_pantalla_x(-2)
        if key == pygame.K_RIGHT:
            self.mapa.set_centro_pantalla_x(2)


    def mouse_posicion(self):
        """Saco la posicion del mouse y la transformo a celda para luego mover al personaje"""
        posXMouse, posYMouse = self.vista.get_mouse_pos()
        posXCeldas = (posXMouse//self.tamanioFotoCelda)+self.largoMinimo # Lo escala al tamaño de las celdas y agrego el corrimiento de la pantalla
        posYCeldas = (posYMouse//self.tamanioFotoCelda)+self.anchoMinimo 
        
        
        
        return (posXCeldas , posYCeldas)

    def setear_pantalla(self):
        """Se setea los limites de la pantalla la cual va a ver el usuario"""
        self.anchoMinimo = self.mapa.getCentroPantalla()[1] - (self.celdasPantallaTotalVertical//2) #40 X
        self.anchoMaximo = self.mapa.getCentroPantalla()[1] + (self.celdasPantallaTotalVertical//2) #60 X
        self.largoMinimo = self.mapa.getCentroPantalla()[0] - (self.celdasPantallaTotalHorizontal // 2) #30 Y
        self.largoMaximo = self.mapa.getCentroPantalla()[0] + (self.celdasPantallaTotalHorizontal // 2) #70 Y
        return self.anchoMinimo, self.anchoMaximo, self.largoMinimo, self.largoMaximo
          

juego = Juego()