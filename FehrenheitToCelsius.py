#Celsius to Fehrenheit Table

def main():

    fahrenheit = 0
    fahrenheit = float(fahrenheit)
    celsius = 0
    celsius = float(celsius)

    print(' F \t\t  C')
    print('----------------------')
    for i in range(0,21,1):
        celsius = i
        fahrenheit = (9/5) * celsius + 32
        print("%.2f" %fahrenheit, '\t\t %.2f' %celsius)


main()
