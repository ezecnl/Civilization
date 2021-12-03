from personaje import Personaje

class Aldeano(Personaje):

    def __init__(self,posicion):
        super().__init__(posicion)
        self.url_imagen="Tropas y personajes/Boy.png"
        
        
    def poder_picar(self):
        return True
        
    

    