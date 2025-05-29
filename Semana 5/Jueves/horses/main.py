from horse import Caballo

def main():
    caballo = Caballo(1, "Palo de agua")
    print(caballo.get_numero())
    caballo.nombre_caballo = "Rayo veloz"
    caballo.set_numero(5)
    print(caballo.get_numero(), caballo.nombre_caballo)

main()