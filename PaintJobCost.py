#Painting Job
#every 115sq.ft = 1gallon & 8hours of labor
#cost = 20/hour of labor,

wallSpace = input('Enter the area of wall to be painted ')
pricePGallon = input('Enter the cost per gallon of paint ')

wallSpace = float(wallSpace)
pricePGallon = float(pricePGallon)

def incrementalCost ():
    gallonsNeeded = wallSpace / 115.0
    reqrdHoursLabor = (8.0 / 115.0) * wallSpace
    costOfPaint = gallonsNeeded * pricePGallon
    laborCharges = reqrdHoursLabor * 20.0
    totalCost = laborCharges + costOfPaint
    print ('Gallons needed to complete the job %.2f ' %gallonsNeeded)
    print ('Number of hours worked %.2f ' %reqrdHoursLabor)
    print ('Cost of paint %.2f ' %costOfPaint)
    print ('Total labor cost %.2f ' %laborCharges)
    print ('Total paint job cost %.2f ' %totalCost)

incrementalCost()
