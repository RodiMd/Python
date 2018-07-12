#Larger than n
#program should accept a list and a number, and should show all
#numbers in the list that are greater than the number

def main():

    numberList = [1, 45, 23, 43, 68, 90, 99, 29, 10, 30]
    number = 51

    results = showGreaterNumbers(numberList, number)

def showGreaterNumbers(nLst, nbr):

    listLength = len(nLst)
    newList = [0] * listLength
    count = 0
    
    for count in range(listLength):
        
        if nbr < nLst[count]:
            print(nLst[count])
            newList[count] = nLst[count]

    print (newList)

main()

