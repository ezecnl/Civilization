from celda import Celda

class Arbol(Celda):
    def __init__(self, is_visible=False) -> None:
        super().__init__(is_visible=False)
        self.vida = 40
        self.cantidadMaderaOtorgada = [60, 20, 10, 30]
        self.url_imagen = "imagenes/arbol_nuevo.png"

    def minado(self):
        pass

