def search(lista, to_find, index):
    if index == len(lista) - 1:
        return lista[index] == to_find
    
    if lista[index] == to_find:
        return True

    return search(lista, to_find, index + 1)


def main():
    lista = [1,2,3,4,5,6,7,8,9]
    to_find = int(input("Please enter a number to find:"))
    result = search(lista, to_find, 0)

    if result:
        print(f"The element {to_find} is present")
    else:
        print(f"The element {to_find} is not present")

main()