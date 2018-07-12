#Number Analysis Program
#Enter a set of numbers and save it to a list then get max and min, average and total

def main():
    try:
        
        numberList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        numberListCpy = numberList
        index = 0
        sumNumbers = 0
        average = 0

        while index < len(numberList):
            inputToList = float(input('Enter a number '))
            numberList[index] = inputToList
            numberListCpy[index] = inputToList
            index+=1
            sumNumbers += inputToList
            
        average = sumNumbers/index
        numberListCpy.sort()
        print('The minimum Number is ',numberListCpy[0])
        print('Tha maximum number is ',numberListCpy[19])
        print('The sum of all variables in the list ',sumNumbers)
        print('The average of the numbers in the list ',average)
    except:
        print('ERROR')
    
##    print(numberList)
##    print(numberListCpy)

main()
