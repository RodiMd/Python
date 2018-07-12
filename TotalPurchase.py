#Total Purchase

snicker = input ('Enter snicker price ')
twix = input ('Enter Twix price ')
toiletPaper = input ('Enter toiletPaper price ')

sumProducts = float(snicker) + float(twix) + float(toiletPaper)
totalTax = 0.06 * float(sumProducts)
Total = sumProducts + totalTax

print ('')
print ('PreTax total is %.2f' %sumProducts)
print ('your total tax is %.2f' %totalTax)
print ('Your total cost is %.2f' %Total)
