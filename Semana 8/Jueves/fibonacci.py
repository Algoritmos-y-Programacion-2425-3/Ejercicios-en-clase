def fibo(num1,num2,number_max):
    if num2 > number_max:
        return
    
    print(num1, end=",")
    fibo(num2,num1+num2,number_max)
    
def main():
    number_max = int(input("Please enter a max number:"))
    fibo(0,1,number_max)
    
main()