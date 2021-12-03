from personaje import Personaje

class Fundador(Personaje):

    def __init__(self,posicion):
        super().__init__(posicion)
        self.url_imagen="Tropas y personajes/Man.png"
        

    def fundar_ciudad(self):
        pass

    def poder_picar(self):
        return False