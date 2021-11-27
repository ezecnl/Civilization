import pygame
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
        self.ir_mapas= False
        self.poder_minar=False
        
        self.jugar()
 
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
                

            if not self.ir_mapas:
                self.vista.menu_principal()
            

            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    self.movimiento_pantalla(event.key)
                    self.vista.limites_actualizados(self.setear_pantalla())#setear nuevos llimites despues de mover la camara
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        if self.juego_empezo== True:
                            print(self.mapa.get_personaje().get_pos(),self.mapa.get_item(self.mouse_posicion()[1],self.mouse_posicion()[0]).get_recurso())
                            if self.mapa.get_item(self.mouse_posicion()[1],self.mouse_posicion()[0]).isSpawn()==True:#no se puede spawnear en los recursos
                                self.poder_minar=True
                                self.mapa.get_personaje().mover_personaje(self.mouse_posicion(),self.mapa)
                                #self.vista.dibujar_personaje(self.mouse_posicion()[1],self.mouse_posicion()[0])
                                
                         
                    elif event.button == 1: 
                        if self.poder_minar==True:
                            
                            self.mapa.get_item(self.mouse_posicion()[1],self.mouse_posicion()[0]).minar(self.mapa.get_personaje())
                            print(self.mapa.get_personaje().inventario)
                            self.vista.mostrar_mapa()
            
            
                      
           

            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(60)
        

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
        celdasX= self.celdasPantallaTotalHorizontal//2
        celdasY= self.celdasPantallaTotalVertical//2
        posXCeldas = (posXMouse//self.tamanioFotoCelda)+self.largoMinimo # Lo escala al tamaño de las celdas
        posYCeldas = (posYMouse//self.tamanioFotoCelda)+self.anchoMinimo
        
        
        #Todo: falta terminar lo de moverse del personaje
        return (posXCeldas , posYCeldas)

    def setear_pantalla(self):
        """Se setea los limites de la pantalla la cual va a ver el usuario"""
        self.anchoMinimo = self.mapa.getCentroPantalla()[1] - (self.celdasPantallaTotalVertical//2) #40 X
        self.anchoMaximo = self.mapa.getCentroPantalla()[1] + (self.celdasPantallaTotalVertical//2) #60 X
        self.largoMinimo = self.mapa.getCentroPantalla()[0] - (self.celdasPantallaTotalHorizontal // 2) #30 Y
        self.largoMaximo = self.mapa.getCentroPantalla()[0] + (self.celdasPantallaTotalHorizontal // 2) #70 Y
        return self.anchoMinimo, self.anchoMaximo, self.largoMinimo, self.largoMaximo
          

juego = Juego()