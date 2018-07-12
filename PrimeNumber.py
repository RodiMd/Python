#Prime Numbers

def main():

    enterPrime = input('Enter a number to see if it is prime ')
    primeValue = is_prime(enterPrime)

def is_prime(intArg):
    intArg = int(intArg)
    num = intArg - 1

    while num >= 1:
        if (intArg % num) == 0 and num > 1:
            print('The entered number', intArg, 'is not a prime number')
            num = 0
            num -= 1
        elif num == 1:
            print ('The entered number' , intArg, 'is a prime number')
            num -= 1
        else:
            num -= 1

main()
