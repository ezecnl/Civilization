from estructura import Estructura

class Casa(Estructura):
    def __init__(self) -> None:
        super().__init__()
        self.costo={"Madera":100,"Piedra":50}
        self.url_imagen="Imagenes/estructura-casa"