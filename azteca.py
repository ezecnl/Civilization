from civilizacion import Civilizacion
class Azteca(Civilizacion):
    def __init__(self):
        super().__init__()
        self.ataque = 30
        self.vida = 100
        self.velocidad = 30
        self.comida = 10
        
