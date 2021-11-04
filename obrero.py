from personaje import Personaje

class Obrero(Personaje):

    def __init__(self):
        self.tarea = None
        self.estructura_a_contruir =["Mina", "Granja", "Corral","Puerto"]
        self.recursos = []
        
    def recolectar(self):
        pass

    def construir_estructura(self):
        pass