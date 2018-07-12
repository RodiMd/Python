#Sum of Digits in a string
#user enter a series of single-digit numbers with nothing
#separating them
#the program should display the sum of all single digit numbers

def main():

    userInputNumber = input('Enter random multiple digits e.g 241589 ')

    numberList = [0] * len(userInputNumber)
    sumOfNumbers = 0
    for count in range(0, len(userInputNumber)):
        numberList[count] = userInputNumber[count]
        print(numberList[count])
        sumOfNumbers += float(numberList[count])

    print('The sum of the entered digits is: ', sumOfNumbers)
        
main()
        

