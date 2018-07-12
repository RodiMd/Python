#Initials


def main():

    first = input('Enter your first name: ')
    middle = input('Enter your middle name: ')
    last = input('Enter your last name')

    personInfo = [first, middle, last]
    print(personInfo)

# the next four lines of code are equivalent to the code below at 1    
    Info0 = first[:1]
    Info1 = middle[:1]
    Info2 = last[:1]
    print(Info0,'.', Info1, '.', Info2)

# the code here including the print are equal to the code above
    Info = [0] * 3
    i = 0
    for i in range(0,3):
        Info[i] = personInfo[i:1]

    print(Info0,'.', Info1, '.', Info2)
    
main()
