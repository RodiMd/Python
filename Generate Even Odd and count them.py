#Odd/Even Scounter
import random

status = True

def main():
    even = 0
    odd = 0
    for i in range(100):
        num = random.randint(1, 100)
        number = even_odd(num)
        if number == True:
            even += 1
            print('even', even, num)
        else:
            odd += 1
            print('\t\t odd', odd, num)
    print ('Even numbers', even, 'Odd numbers', odd)
    
def even_odd(evenOdd):
    if (evenOdd % 2) == 0:
        status = True
    else:
        status = False
    return status

main()
