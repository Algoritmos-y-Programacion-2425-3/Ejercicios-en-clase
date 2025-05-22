def average(numbers):
    acum = 0
    for number in numbers:
        acum += number
    return acum/len(numbers)

def main():
    lista = [1,2,3,4,5]
    result = average(lista)
    print(result)

main()