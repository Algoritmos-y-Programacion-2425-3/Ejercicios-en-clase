def decrypt(code, k):  
    code_copy = []
    for i in range(len(code)):
        cont = 1
        acum = 0
        while cont <= k:
            acum += code[(i + cont)%len(code)]
            cont += 1
        code_copy.append(acum)
    return code_copy

def main():
    code = [5,7,1,4]
    k = 3
    lista = decrypt(code, k)
    print(lista)

main()