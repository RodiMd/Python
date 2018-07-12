#Math Quiz
#two random numbers to be added and the student should
#be allowed to respond, if correct then congrats
#if answer is incorrect - learn some math

import random #if want to use random number generation


def main():
    ranNum1 = random.randint(1,1000)
    ranNum2 = random.randint(1,1000)
    print(ranNum1, "+", ranNum2)
    sumEnt = input('Enter the sum of the two numbers ')
    sumEnt = int(sumEnt)
    sumRandNum = add_random_numbers(ranNum1, ranNum2)
    sumRandNum = int(sumRandNum)
    
    if sumEnt == sumRandNum:
        print('You passed your math quiz ', sumRandNum)
    else:
        print('Better learn some more math')
        print('The correct answer is ', sumRandNum)

def add_random_numbers(num1, num2):
    return num1 + num2
main()
