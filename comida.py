from recurso import Recurso

class Comida(Recurso):
    def __init__(self,cantidad) -> None:
        super().__init__(cantidad)