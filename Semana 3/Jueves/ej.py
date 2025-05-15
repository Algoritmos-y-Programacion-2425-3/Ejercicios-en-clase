number = int(input("Please enter a number: "))
is_prime = True
if number <= 1:
    is_prime = False

for i in range(2,number):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"The number {number} is prime")
else:
    print(f"The number {number} is not prime")