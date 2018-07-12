# Areas of Rectangels

lengthFRectangle1 = input('Enter the length of rectangle one ')
widthFRectangle1 = input('Enter the width of rectangle one ')
lengthFRectangle2 = input('Enter the length of rectangle two ')
widthFRectangle2 =input('Enter the width of rectangle two ')

#indentation is very important, if indentation is not correct the program may not
#work. if something in the function all have to be indented inside
#if another function inside then inside it should be even more indented
def main():
    areaOne = float(lengthFRectangle1) * float(widthFRectangle1)
    areaTwo = float(lengthFRectangle2) * float(widthFRectangle2)
    areaOne = float(areaOne)
    areaTwo = float(areaTwo)
    
    print ('Area1 is ', areaOne, '& Area2 is ',areaTwo)
    
    if areaOne > areaTwo:    
        print('Area1 ', areaOne, ' is greater than Area2 ', areaTwo)
    elif areaTwo > areaOne:
        print('Area2 ', areaTwo, ' is greater than Area1 ', areaOne)
    elif areaOne == areaTwo or areaTwo == areaOne:
        print('you should enter different values to capture the intent of the program ')
    else:
        print('you should enter different values to capture the intent of the program ')
    
main()


