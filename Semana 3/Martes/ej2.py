while True:
    number = input("Please enter a number to validate or -1 to exit:")
    if number == "-1": 
        break
    else:
        if number.isnumeric():
            number = int(number)
            aux = 2
            is_prime = True
            while aux < number:
                if number % aux == 0:
                    is_prime = False
                    break
                aux += 1
            if is_prime:
                print(f"The number {number} is prime")
            else:
                print(f"The number {number} is not prime")

        else:
            print("Error!!")
