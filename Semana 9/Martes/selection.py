def selection(lista):
    for index in range(len(lista)):
        minor = index
        for j in range(index+1,len(lista)):
            if lista[j] < lista[minor]:
                minor = j
        temp = lista[index]
        lista[index] = lista[minor]
        lista[minor] = temp

def main():
    lista = [6,5,3,1,8,7,2,4]
    selection(lista)    
    print(lista)

main()