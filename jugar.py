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
        self.vista = Vista(self,self.mapa,self.celdasPantallaTotalHorizontal, self.celdasPantallaTotalVertical, self.tamanioFotoCelda, self.anchoLargoPantalla)
        self.juego_empezo = False
        self.ir_mapas= False
        self.jugar()
 
    def empezar_juego(self):
        self.juego_empezo = True

    def menu_mapa(self):
        self.ir_mapas= True

    def jugar(self):
        while True: 
            if not self.juego_empezo:#para que los menus se queden en la pantalla
               self.vista.menu_mapa()
            if not self.ir_mapas:
                self.vista.menu_principal()
            
            for event in pygame.event.get():
                rightClicking = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    self.movimiento_pantalla(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mapa.get_personaje().mover_personaje(self.mouse_posicion())
                    elif event.button == 3: 
                        pass

            #self.vista.mostrar_mapa()
            #self.vista.mostrar_jugador()            
           

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
        posXCeldas = (posXMouse//self.tamanioFotoCelda) # Lo escala al tamaño de las celdas
        posYCeldas = (posYMouse//self.tamanioFotoCelda)
        #Todo: falta terminar lo de moverse del personaje
        return (posXCeldas , posYCeldas)

          

juego = Juego()