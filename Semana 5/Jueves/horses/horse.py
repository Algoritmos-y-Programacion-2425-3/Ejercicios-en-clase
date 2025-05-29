class Caballo:
    def __init__(self, numero, nombre):
        self.__numero = numero
        self.nombre_caballo = nombre

    def get_numero(self):
        return self.__numero
    
    def set_numero(self, nuevo_numero):
        self.__numero = nuevo_numero