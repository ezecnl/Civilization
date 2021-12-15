class Recurso:
    def __init__(self,cantidad) -> None:
        self.cantidad=cantidad
    
    def  __add__(self,otro):
        self.cantidad += otro

    def get_cantidad(self):
        return self.cantidad