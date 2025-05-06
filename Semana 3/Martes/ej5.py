number = int(input("Please enter a number: "))
cont = 0
aux = 1
while cont < number:
    cont += 1
    if aux == 1:
        print(aux)
    else: 
        print(aux, end = " ")
    aux2 = aux
    while aux2 > 1:
        aux2 -= 2
        if aux2 == 1:
            print(aux2)
        else: 
            print(aux2, end = " ")
    aux += 2