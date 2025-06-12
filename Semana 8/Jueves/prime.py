def is_prime(number, aux):
    if number % aux == 0:
        return False 
    
    if aux == number - 1:
        return True

    return is_prime(number, aux + 1)


def main():
    number = int(input("Please enter a number to find:"))
    result = is_prime(number, 2)

    if result:
        print(f"The element {number} is prime")
    else:
        print(f"The element {number} is not prime")

main()