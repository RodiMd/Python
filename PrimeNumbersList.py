#make a list of all prime numbers from 1 to 100

def main():
    val = int(0)
    val2 = int(0)

    for val in range(100):
        primeNum = is_prime(val)
        
def is_prime(num):


    num2 = num - 1
    while num2 >= 1:
    
        if (num % num2) == 0 and num2 > 1:
            print('The entered number', num, 'is not a prime number')
            num2 = 0
            num2 -= 1
        elif num2 == 1:
            print ('The entered number' , num, 'is a prime number')
            num2 -= 1
        else:
            num2 -= 1
    return num, num2

main()

