

class Celda:
    def __init__(self):
        self.tamañaoCelda = 20
        self.recurso= None#fuente_de_recurso
        self._sprite = None
        self.url_imagen = None
        self.personaje = None
        self.estructura= None

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
    
    
    def get_recurso(self):
        
        return self.recurso
    
    def set_personaje(self, personaje):
        self.personaje = personaje
        

    def eliminar_personaje(self):
        self.personaje=None

    

    def hayRecurso (self):
        if self.recurso:
            return True
        else:
            return False


    def get_personaje(self):
        return self.personaje
    
    def minar(self, personaje):
        """agrega en el inventario del personaje el recuro minado y lo saca de su celda"""
        tipo,cantidad=self.recurso.minado() #el recurso cuando se inicie el juego valdra algo
        personaje.agregar_inventario(tipo, cantidad)
        if self.recurso.vida != 0:
            self.recurso.adquirir()
        else:
            self.recurso=None

   

    def get_estructura(self):
        return self.estructura

    def set_estructura(self,estructura):
        self.estructura = estructura
        

        
        
        
        


 