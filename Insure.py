#How Much Insurance
#should ensure your property for atleast 80 percent of the cost
#to replace it

costToReplace = input('Enter the amount it would cost to replace it ')

def minInsurance():
    amountToInsure = 0.8 * float(costToReplace)
    print ('amount to insure is %.2f' %amountToInsure)

minInsurance()
