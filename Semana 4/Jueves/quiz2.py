number = int(input("Please enter a number:"))
acum = 0
for aux in range(1,number):
    if number % aux == 0:
        acum += aux

print(acum > number)