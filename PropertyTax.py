#Property Tax
#60% of actual property value
#if and acre is 10000, the assessment is 6000,
#tax = 0.64 for each $100 of the assessment.
#tax on 6000 is 38.4

propertyValue = input('Enter the value of the property ')
costPerHundred = 0.64
propertyValue = float(propertyValue)

def main():
    assessedValue = 0.6 * propertyValue
    totalTax = 0.64 * (propertyValue/100.0)
    print ('The assessed value of property is %.2f' %assessedValue)
    print ('The total property tax is %.2f' %totalTax)

main()
