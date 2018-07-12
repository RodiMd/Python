#Stock transaction program

shares = 1000
shares = float(shares)
IntlPaidperShare = 32.87
commissionOfStockPrice = 0.02

time = 2 #weeks
sharesSold = 1000
sharesSold = float(sharesSold)
fnlSharePrice = 33.92
commissionStockSalePrice = 0.02

#write a program that displays
#amount paid for stock
#amount of commission paid to broker when bought stocks
#amount of sale of stocks
#commission paid upon sale of stock
#remaining after all payments made

totalCostofStockBuy = shares * IntlPaidperShare
commissionPaidForPurchase = commissionOfStockPrice * totalCostofStockBuy
soldSharesForTheTotalAmount = fnlSharePrice * sharesSold
commissionPaidforSale = fnlSharePrice * sharesSold * commissionStockSalePrice
totalCommissionPaid = commissionPaidForPurchase + commissionPaidforSale
remainingBalance  = soldSharesForTheTotalAmount - totalCostofStockBuy - totalCommissionPaid

print ('total Paid for stock purchase ', totalCostofStockBuy)
print ('total commissions paid for purchasing ', commissionPaidForPurchase)
print ('total received for sale of shares ', soldSharesForTheTotalAmount)
print ('commission total paid to broker ', commissionPaidforSale)
print ('remaining balance (Gain/Loss) %.2f' %remainingBalance)
