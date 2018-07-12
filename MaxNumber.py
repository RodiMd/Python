#Max of two values
#write a function called max, accepts two integers and returns
#the greater value

def main():
    print('Enter two values that will then be compared')
    val1 = input('Enter the first number you want to compare')
    val2 = input('Enter the second number you want to compare')

    maxValue = max(val1, val2)

def max(num1, num2):
    if num1 > num2:
        print(num1, ' is greater than ', num2)
    else:
        print (num2, ' is greater than ', num1)

main()


