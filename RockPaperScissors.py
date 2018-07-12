#Rock Paper & Scissors
#play against the computer
#random number generation 1-3, if 1=rock,2=paper,3=scissors
#dont display computer choice just yet
#user enters choice
#display comp choice
#winner is selected
#rock wins over scissors, scissors wins over paper, paper wins over rock
#if same choice play again

import random
rock = ''
scissors = ''
paper = ''


def main():
    global rock
    global scissors
    global paper
    result = ''
    playerChoice = ''
    while result == playerChoice:
        randNumber = random.randint(1, 3)
        playerChoice = input('Enter your choice, paper, rock, scissors ')
        result = comp_Choice (randNumber)
        winner = result_game (result, playerChoice)        
    
def comp_Choice(rN):
    
    if rN == 1:
        rN = str('rock')
    elif rN == 2:
        rN = str('scissors')
    else:
        rN = str('paper')
    return rN

def result_game(rC, pC):
    
    if pC == 'rock' and rC == 'scissors':
        print('The winner is user', pC)
    elif pC == 'scissors' and rC == 'rock':
        print ('The winner is the computer ', rC)
        
    elif pC == 'scissors' and rC == 'paper':
        print('The winner is the user ', pC)
    elif pC == 'paper' and rC == 'scissors':
        print('The winner is the computer ', rC)
        
    elif pC == 'paper' and rC == 'rock':
        print('The winner is the user ', pC)
    elif pC == 'rock' and rC == 'paper':
        print('The winner is the computer ', rC)

    else:
        print('The result is a tie ', pC, '&', rC)
    
main()
    
