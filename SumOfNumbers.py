#Sum Numbers
#ask user to enter a series of positive numbers
#to end series, the user should enter a negative number
#compile sum of all positive numbers

def main():
    print('To terminate the program, enter a negative number')
    condition = 'y'
    condition = str(condition)
    positiveNumber = 0
    positiveNumber = int(positiveNumber)
    
    while condition == 'y':
        positiveNumber2 = input('Enter a positive number ')
        positiveNumber2 = int(positiveNumber2)
        positiveNumber += positiveNumber2

        if positiveNumber2 < 0 :
            condition = 'n'
            positiveNumber -= positiveNumber2 #this subtracts the last -negative number entered
    print('The sum of entered numbers is ', positiveNumber)
    
main()
        
