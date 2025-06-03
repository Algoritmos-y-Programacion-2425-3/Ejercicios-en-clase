class Participante:
    n_participantes = 0
    def __init__(self, nombre, esSolista, categoria, n_telefono: str, n_registro):
        Participante.n_participantes += 1
        self.nombre = nombre
        self.esSolista = esSolista
        self.categoria = categoria
        self.n_telefono = "No tiene" if n_telefono.isspace() or n_telefono == "" else n_telefono
        self.n_registro = n_registro

    def mostrar_info(self):
        return f"""
        Nombre: {self.nombre}
        Es Solista: {"Si" if self.esSolista else "No"}
        Categoría: {self.categoria}
        Teléfono: {self.n_telefono}
        Número de Registro: {self.n_registro}
        """
