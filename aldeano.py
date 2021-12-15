from personaje import Personaje

class Aldeano(Personaje):

    def __init__(self,posicion):
        super().__init__(posicion)
        self.url_imagen="Tropas y personajes/Boy.png"
        
        
    def consumir_recurso(self,recurso):
        tipo,cantidad=recurso.adquirir() #el recurso cuando se inicie el juego valdra algo
        self.agregar_inventario(tipo, cantidad)        
    

    