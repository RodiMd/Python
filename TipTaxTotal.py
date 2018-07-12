#Tips, Tax, Total
#calculate cost of meal
#ask for charge for food
#calculate 15% tips and 7% tax
#display each amount and total

foodCost = input('How much was the food ')
foodCost = float(foodCost)
tip = 0.15 * foodCost
tax = 0.07 * foodCost

total = foodCost + tip + tax
print ('Food cost %.2f' %foodCost)
print ('total tip %.2f' %tip)
print ('total tax %.2f' %tax)
print ('Total bill %.2f' %total)

#or

print('Food cost %.2f' %foodCost+ '\n'+
      'Total tip %.2f' %tip +'\n'+
      'Total tax %.2f' %tax +'\n' +
      'Total bill %.2f' %total)


