#Book club points
# the club awards points based on books purchased per month
#1book = 5points, 2=15points, 3=30points, 4=60points

numberFBooks = input('Enter the quantity of books purchased this month ')
numberFBooks = int(numberFBooks)

def main():

    if numberFBooks == 0:
        print('Poitns earned this month are 0')
    elif numberFBooks == 1:
        print ('Points earned this month are 5')
    elif numberFBooks == 2:
        print ('Points earned this month are 15')
    elif numberFBooks == 3:
        print ('Points earned this month are 30')
    elif numberFBooks == 4:
        print('Points earned this month are 60')
    else:
        print('You have entered a value outside of what we have')
        
main()
