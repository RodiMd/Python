#Random Number Guessing Game
#write a program that generates random numbers 1-100
#ask user to guess number, if guess is high 'too high, try again'
#if too low 'too low, try again', if guessed, then congrats and
#generate a new number to restart the game

import random

guessNumber = 0
count = 0
def main():
    global guessNumber
    randNumber = random.randint(1,100)
    print(randNumber)
        
    while guessNumber != randNumber:
        guessNumber = input('Guess a number between 1 and 100 ')
        result = guess_condition(guessNumber, randNumber)
        

def guess_condition(GN, RN):
    GN = int(GN)
    RN = int(RN)
    global count
    
    if GN > RN:
        print('The number guessed is too high, try again ')
        count+=1
    elif GN < RN:
        print('The number guessed is too low, try again ')
        count+=1
    elif GN == RN:
        print('Congrats, the guessed number is correct ')
        count+=1
        print(count)

##def guess_loop():
##    while GN != RN:
        
main()
