from personaje import Personaje

class Guerrero(Personaje):

    def __init__(self,posicion):
        super().__init__(posicion)
        self.url_imagen="Tropas y personajes/GraveRobber.png"

    def poder_picar(self):
        return False