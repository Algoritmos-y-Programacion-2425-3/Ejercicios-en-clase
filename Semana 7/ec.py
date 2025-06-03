class Libro:
    def __init__(self, author, title, pages):
        self.author = author
        self.title = title 
        self.pages = pages

    def mostrar_info(self):
        print(f"Title:{self.title}, Author:{self.author}, pages:{self.pages}")

    def es_extenso(self, umbral):
        return self.pages > umbral
    
def main():
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 432)
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)

    libro1.mostrar_info()
    print(f"Es extenso: {libro1.es_extenso(300)}")
    
    libro2.mostrar_info()
    print(f"Es extenso: {libro2.es_extenso(300)}")
    

main()