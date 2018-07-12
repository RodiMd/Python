#Roman Numerals
#prompt user to enter a value between 1 and 10.

number = input('Enter a number between 1 and 10 ')
number = float(number)

def main():

    if number == 1:
        print('The value entered ', number, 'has a roman equivalent of I')
    else:
        if number == 2:
            print('The value entered ', number, 'has a roman equivalent of II')
        else:
            if number == 3:
                print('The value entered ', number, 'has a roman equivalent of III')
            else:
                if number == 4:
                    print('The value entered ', number, 'has a roman equivalent of IV ')
                else:
                    if number == 5:
                        print('The value entered ', number, 'has a roman equivalent of V ')
                    else:
                        if number == 6:
                            print('The value entered ', number, 'has a roman equivalent of VI')
                        else:
                            if number == 7:
                                print('The value entered ', number, 'has a roman equivalent of VII')
                            else:
                                if number == 8:
                                    print('The value entered ', number, 'has a roman equivalent of VIII')
                                else:
                                    if number == 9:
                                        print('The value entered ', number, 'has a roman equivalent of IX')
                                    else:
                                        if number == 10:
                                            print('The value entered ', number, 'has a roman equivalent of X')
                                        else:
                                            print('Error: The value entered ', number, 'is outside the specified range')

main()
        
