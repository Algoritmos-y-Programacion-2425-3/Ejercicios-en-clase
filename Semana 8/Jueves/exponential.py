def exponential(base, exp):#2,3 / 2,2 / 2,1
    if exp == 1:
        return base
    
    return base * exponential(base, exp - 1) 
# 2 * exponential(2, 2) / 2 * 2 * 2 
# 2 * exponential(2, 1) / 2 * 2
#  2

def main():
    result = exponential(int(input("Please enter the base:")), int(input("Please enter the exp:")))
    print(result)

main()