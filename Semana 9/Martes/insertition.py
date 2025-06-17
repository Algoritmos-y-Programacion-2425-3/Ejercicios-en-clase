def insertition(lista):
    for index, value in enumerate(lista):
        j = index - 1
        while j >= 0 and value < lista[j]:
            lista[index] = lista[j]
            lista[j] = value
            index -= 1
            j -= 1

def main():
    lista = [6,5,3,1,8,7,2,4]
    insertition(lista)    
    print(lista)

main()