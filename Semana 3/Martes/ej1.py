word = input("Please enter a word:")
cont = 0
max_attempts = 10
"""
while cont < max_attempts:
    print(word)
    cont += 1
"""


while True:
    print(word)
    cont += 1
    if cont == max_attempts:
        break