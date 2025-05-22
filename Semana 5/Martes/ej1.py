def factorial(numero):
    acum = 1
    for number in range(1,numero+1):
        acum *= number
    return acum

def main():
    print("Welcome to factorial")
    number = int(input("Please enter a number"))
    result = factorial(number)
    print(f"{number}! = {result}")

main()