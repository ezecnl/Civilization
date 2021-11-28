from personaje import Personaje

class Aldeano(Personaje):

    def __init__(self,posicion):
        super().__init__(posicion)
        self.url_imagen="Tropas y personajes/Boy.png"
        self.estructura_a_contruir =["Mina", "Granja", "Corral","Puerto"]
        
        
    def recolectar(self):
        pass

    def construir_estructura(self):
        pass