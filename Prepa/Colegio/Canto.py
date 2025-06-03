from Participante import Participante

class Canto(Participante):
    n_cantos = 0
    def __init__(self, nombre, esSolista, categoria, n_telefono: str, n_registro, titulo_cancion, autor_cancion):
        Canto.n_cantos += 1
        super().__init__(nombre, esSolista, categoria, n_telefono, n_registro)
        self.titulo_cancion = titulo_cancion
        self.autor_cancion = autor_cancion

    def mostrar_info(self):
        return super().mostrar_info() + f"""
        Canción: {self.titulo_cancion} - {self.autor_cancion}
        Tipo: Canto
        """