from civilizacion import Civilizacion
class Inca(Civilizacion):
    def __init__(self):
        super().__init__()
        self.ataque = 30
        self.vida = 100
        self.velocidad = 30
        self.comida = 10

    """aumenta el radio de vision"""
    def ver_bloques(self):
        pass
    