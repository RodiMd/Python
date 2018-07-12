#random number file reader

def main():
    readFile = open(r'C:\Users\Rodi\Desktop\PythonPrograms\randomNumber.txt', 'r')
    fileContent = readFile.read()
    print(fileContent)
    readFile.close()

    readFile = open('randomNumber.txt', 'r')
    rowContent = readFile.readline()

    sumRow = 0
    count = 0
    while rowContent != '':
        rowNumber = float(rowContent) #convert line content to float
        sumRow += rowNumber
        count += 1

        rowContent = readFile.readline()

        
    print (count)        
    print(sumRow)
    readFile.close()


main()
