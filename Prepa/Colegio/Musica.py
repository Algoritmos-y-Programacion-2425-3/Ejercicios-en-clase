from Participante import Participante

class Musica(Participante):
    n_musica = 0
    def __init__(self, nombre, esSolista, categoria, n_telefono: str, n_registro, instrumentos):
        Musica.n_musica += 1
        super().__init__(nombre, esSolista, categoria, n_telefono, n_registro)
        self.instrumentos = instrumentos

    def mostrar_info(self):
        return super().mostrar_info() + f"""
        Instrumentos: {self.instrumentos}
        Tipo: Música
        """