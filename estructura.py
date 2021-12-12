
class Estructura:
    def __init__(self,x,y) -> None:
        self.costo={"Madera":0,"Piedra":0}
        self.url_imagen = None
        self._sprite = None
        self.posX = x
        self.posY = y

    def set_sprite(self, sprite):
        """Seteo el sprite"""
        self._sprite = sprite

    def get_url_imagen(self):
        """Obtengo la url de la imagen que voy a cargar y la devuelo"""
        return self.url_imagen

    def get_sprite(self):
        """devuelvo el sprite"""
        return self._sprite

    