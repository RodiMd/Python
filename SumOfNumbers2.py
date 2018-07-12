#sum Numbers


def main():
    try:
        numbersFile = open('numbers2.txt', 'r')
        readNumbers = numbersFile.readline()
        count = 0
        valNumbers = 0
        sumNumbers = 0

        while readNumbers != '':

                try:
                    valNumbers = int(readNumbers)
                    sumNumbers += valNumbers
                    count+=1
                    average = sumNumbers / count
                    readNumbers = numbersFile.readline()
                    
                except ValueError as err:
                    print()

        print ('The sum of the numbers is ', sumNumbers)
        print ('The average of the numbers is ', average)
        numbersFile.close()
        
        numbersFile = open('numbers2.txt', 'r')
        seeFile = numbersFile.read()
        print(seeFile)
        numbersFile.close()
        
    except IOError:
        print('The specified file could not be read or found', 'numbers2.txt')
main()
