from Participante import Participante

class Libre(Participante):
    n_libres = 0
    def __init__(self, nombre, esSolista, categoria, n_telefono: str, n_registro, talento):
        Libre.n_libres += 1
        super().__init__(nombre, esSolista, categoria, n_telefono, n_registro)
        self.talento = talento

    def mostrar_info(self):
        return super().mostrar_info() + f"""
        Talento: {self.talento}
        Tipo: Libre
        """