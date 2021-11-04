from celda import Celda


class Arbusto(Celda):
    def __init__(self, is_visible=False) -> None:
        super().__init__(is_visible=False)
        self.vida = 30
        self.cantidadComidaOtorgada = [60, 20, 50, 70, 35]
        self.url_imagen= "imagenes/arbusto_nuevo.png"

    def minado(self):
        pass



