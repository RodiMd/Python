#Sales TAx Program Refractoring
#write this program using functions

amountOfPurchase = input('Enter the amount of purchase ')
amountOfPurchase = float(amountOfPurchase)

def main():
    stateLocalTax()

def stateLocalTax():
    taxRate = 0.04
    stateTaxTotal = amountOfPurchase * taxRate
    taxRate = 0.02
    countyTaxTotal = amountOfPurchase * taxRate
#x - x used to reference the comments below as how local variable
#values were passed to another function.    
    totalCost(stateTaxTotal, countyTaxTotal)

#totalCost - gets stateTax and countyTax local variable values from
#stateLocalTax function, but to be done it has to be set in the function
#that calls the new function as done in stateLocalTax at location
#x, at x the line of code sets the values to be passed to the totalCost function
    
def totalCost(stateTax, countyTax):
    totalCost = countyTax + stateTax + amountOfPurchase
    print ('total state tax %.2f' %stateTax)
    print('total county tax %.2f' %countyTax)
    print ('Total cost is %.2f ' %totalCost)
    
main()

