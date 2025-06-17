def quicksort(lista):
    if len(lista) < 2:
        return lista

    menores, pivote, mayores = partition(lista)
    return quicksort(menores) + [pivote] + quicksort(mayores)
    
def partition(lista):
    menores = []
    mayores = []
    pivote = lista[0]
    for number in lista:
        if number < pivote:
            menores.append(number)
        elif number > pivote:
            mayores.append(number)
    return menores, pivote, mayores

def main():
    lista = [6,5,3,1,8,7,2,4]
    lista = quicksort(lista)    
    print(lista)

main()