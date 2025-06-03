from Participante import Participante

class Baile(Participante):
    n_bailes = 0
    def __init__(self, nombre, esSolista, categoria, n_telefono: str, n_registro, estilo):
        Baile.n_bailes += 1
        super().__init__(nombre, esSolista, categoria, n_telefono, n_registro)
        self.estilo = estilo

    def mostrar_info(self):
        return super().mostrar_info() + f"""
        Estilo de Baile: {self.estilo}
        Tipo: Baile
        """