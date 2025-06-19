from estudio import Estudio
from cliente import Cliente
from factura import Factura

def welcome():
    print("Bienvenido a la clinica Caracas!!")

def option_study():
    option = int(input("Please enter the study you want: 1-Ultrasonido, 2- Tomografia, 3- Resonancia"))
    return option

def get_customer():
    return Cliente(
        input("Please enter your dni: "),
        int(input("Please enter your age: ")),
        input("Please enter your gender M or F: "),
        input("Please enter if you have an inssurance 1-yes,2-No: ") == "1",   
    )

def print_factura(factura):
    print("******* FACTURA ********")
    print(f"Cedula: {factura.cliente.cedula}")
    print(f"Edad: {factura.cliente.edad}")
    print(f"Genero: {factura.cliente.genero}")
    print(f"Estudio: {factura.estudio.nombre}")
    print(f"Tiene Seguro: {factura.cliente.tiene_seguro}")
    print(f"Descuentos: {factura.descuento}")
    print(f"Total: {factura.total}")


def get_discount(base_amount, edad, tiene_seguro, genero):
    discount = 0.0
    if tiene_seguro:
        discount += base_amount * 0.8
    if edad >= 70 and genero == "F":
        discount += base_amount * 0.2
    if edad >= 80 and genero == "M":
        discount += base_amount * 0.15

    return discount

def main():
    studies = [
        Estudio("Ultrasonido",8.90),
        Estudio("Tomografía",12.64),
        Estudio("Resonancia",15.60)
    ]
    welcome()
    facturas = []
    while True:
        option = option_study()
        study = studies[option -1]
        customer = get_customer()
        base_amount = (customer.edad*10) + study.precio_base
        discount = get_discount(base_amount, customer.edad, customer.tiene_seguro, customer.genero)  
        total = base_amount - discount
        factura = Factura(
            customer,
            study,
            discount,
            total
        )
        print_factura(factura)
        facturas.append(factura)


main()