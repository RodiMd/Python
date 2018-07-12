#Mass and Weight

mass = input('Enter a mass in kilograms to obtain its weight ')
mass = float(mass)

def main():
    weight = mass * 9.8
    
    if weight > 1000:
        print('The weight in Newtons is %.2f ' %weight, 'and that is heavy ')
    else:
        if weight < 10:
            print('The weight in Newtons is %.2f ' %weight, 'and that is light ')
        else:
            print ('The weight in Newtons is %.2f' %weight)
main()
