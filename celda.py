

class Celda:
    def __init__(self, is_visible=True):
        # TODO: areglar lo de que no se vea el mapa
        self.visible = is_visible
        self.tamañaoCelda = 20
        self.objetos = []
        self.recurso= None
        self._sprite = None
        self.url_imagen = None
        self.personaje = None

    def set_sprite(self, sprite):
        self._sprite = sprite

    def get_url_imagen(self):
        return self.url_imagen

    def get_sprite(self):
        return self._sprite
    
    def get_tamaño(self):
        return self.tamañaoCelda

    def hayCuidad(self):
        pass
    
    def visibilizar(self):
        self.visible = False
    
    def get_recurso(self):
        return self.recurso
    
    def set_personaje(self, personaje):
        self.personaje = personaje

    def eliminar_personaje(self):
        self.personaje=None

    

    def isSpawn (self):
        if not self.recurso:
            return True
        else:
            return False


    def get_personaje(self):
        return self.personaje
    
    def minar(self):
        recurso_minar=self.get_recurso()
        tipo,cantidad=recurso_minar.minado()
        self.recurso=None
        return tipo, cantidad
        
        #lacelda= mapa.get_item(PosX,Posy)
        


 