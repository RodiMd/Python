#Sales Tax
#ask amount of purchase
#compute state and county sales tax, state 4% a,d county 2%
#display, purchase amount, state tax, county tax, total tax, total purchase including tax

purchaseAmount = input('Enter purchase amount ')
stTax = 0.04
cntyTax = 0.02

totalStTx = float(purchaseAmount) * stTax
totalCntyTx = float(purchaseAmount) * cntyTax

purchaseTotal = float(purchaseAmount) + totalStTx + totalCntyTx

print ('Total state tax %.2f' %totalStTx)
print ('Total county tax %.2f' %totalCntyTx)
print ('Total purchase Amount %.3f' %purchaseTotal)

#print ('ttl St Tx' totalStTx +'\n'+
        #'ttl Cnty Tx' totalCntyTx +'\n'+
        #'ttl purchase amount ' purchaseTotal)
