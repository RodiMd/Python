#Random Number file Writer
import random

def main():
    
    maxNumbers = input('How many numbers do you want the file to hold? ')
    maxNumbers = int(maxNumbers)
    randNmbrFile = open('randomNumber.txt', 'w')
##    count = 0
    
    for count in range(0, maxNumbers):
        count += 1
        rndNumber = random.randint(1,500)
        randNmbrFile.write(str(rndNumber)+'\n')

    randNmbrFile.close()

    randNmbrFile = open('randomNumber.txt', 'r')
    readRow = randNmbrFile.readline()

    sumRows = 0
    count = 0

    while readRow != '':
        lineRead = float(readRow)
        print(lineRead)
        sumRows += lineRead
        count += 1
        readRow = randNmbrFile.readline()
        
    print (sumRows)
    randNmbrFile.close()
    
    
main()
        
        
