#Gold Scores

def main():
    try:
        nmbrPlayers = int(input('Enter the number of players '))
        scoreFile = open('golf.txt', 'w')
        scoreFile.write('#\t\t Player \t Score'+'\n')
        scoreFile.write('------------------------------------------'+'\n')
        nbr = 1
        
        for i in range(1, nmbrPlayers + 1, 1):
            print(i)
            name = input('Enter the name of the player ')
            score = input('Enter his/her score ')
            scoreFile.write(str(i) + '\t\t  ' + name + '\t\t  '+ str(score)+'\n')
            
        scoreFile.close()

        scoreFile = open('golf.txt', 'r')
        seeFile = scoreFile.read()
        print(seeFile)
        scoreFile.close()
        
    except IOError:
        print('The file does not exist golf.txt')

main()


    
