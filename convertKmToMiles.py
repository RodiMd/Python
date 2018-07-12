#Kilometer Converter
#write a program that converts km to mi

#ask the user to enter a distance in km
distanceKilometers = input('Enter a distance in km ')
distanceKilometers = float(distanceKilometers)
def conversionTokilometers():
    miles = distanceKilometers * 0.6214
    print ('The distance entered in kilometers is %.2f' %miles, 'miles')

conversionTokilometers()
