from Canto import Canto
from Baile import Baile
from Musica import Musica
from Libre import Libre
from Participante import Participante

class App:
    def __init__(self):
        self.participantes = []
    
    def crear_participante(self):
        nombre = input("Ingresa el nombre: ")

        esSolista = input("Ingresa 1 si es solista: ")
        esSolista = True if esSolista == "1" else False

        categoria = input("Ingresa la categoría: ")
        n_telefono = input("N° teléfono: ")
        n_registro = input("n° registro: ")
        return nombre, esSolista, categoria, n_telefono, n_registro

    def crear_canto(self):
        nombre, esSolista, categoria, n_telefono, n_registro = self.crear_participante()
        titulo_cancion, autor_cancion = input("Título y autor de canción separado por comas: ").split(',')
        self.participantes.append(
            Canto(nombre, esSolista, categoria, n_telefono, n_registro, titulo_cancion, autor_cancion)
        )

    def crear_baile(self):
        nombre, esSolista, categoria, n_telefono, n_registro = self.crear_participante()
        estilo_baile = input("Estilo de Baile: ")
        self.participantes.append(
            Baile(nombre, esSolista, categoria, n_telefono, n_registro, estilo_baile)
        )

    def crear_musica(self):
        nombre, esSolista, categoria, n_telefono, n_registro = self.crear_participante()
        instrumentos = input("Instrumentos separados por coma: ").split(',')
        self.participantes.append(
            Musica(nombre, esSolista, categoria, n_telefono, n_registro, instrumentos)
        )
    
    def crear_libre(self):
        nombre, esSolista, categoria, n_telefono, n_registro = self.crear_participante()
        talento = input("Talento: ")
        self.participantes.append(
            Libre(nombre, esSolista, categoria, n_telefono, n_registro, talento)
        )

    def start(self):
        while True:
            print("""
            1. Crear un participante de Canto
            2. Crear un participante de Baile
            3. Crear un participante de Música
            4. Crear un participante de Libre
            5. Cerrar el programa y mostrar los datos
            """)

            n = input("Ingrese un número: ")
            if n == "1":
                self.crear_canto()
            elif n == "2":
                self.crear_baile()
            elif n == "3":
                self.crear_musica()
            elif n == "4":
                self.crear_libre()
            elif n == "5":
                break
            else:
                print("Ingresa un número válido")

        print(f"""
        Número de Participantes: {Participante.n_participantes}
            De canto: {Canto.n_cantos}
            De Baile: {Baile.n_bailes}
            De Música: {Musica.n_musica}
            De Libre: {Libre.n_libres}
        """)

        for participante in self.participantes:
            print(participante.mostrar_info())