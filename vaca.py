from celda import Celda
from tierra import Tierra


class Vaca(Celda):
    def __init__(self) -> None:
        super().__init__(Tierra, is_visible=False)
        self.vida = 25
        self.tiempoParaMatar = 10
        self.cantidadComidaOtorgada = [60, 50, 70]

    

    def muerta(self):
        pass

    def domesticada(self):
        pass

