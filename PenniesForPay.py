#Pennies fot Pay
#the pay per day is a penny and doubles every day, 1,2,4,8,16
#ask user for the number of days
#display each day's salary and total pay at end of period.

nmbrFDays = input('Enter the number of days in a pay period ')
nmbrFDays = int(nmbrFDays)

def main():

    payPerDay = 1
    payPerDay = float(payPerDay)
    payNDlrs = 0
    payNDlrs = float(payNDlrs)
    totalPayNDlrs = 0
    totalPayNDlrs = float(totalPayNDlrs)

    for i in range(0, nmbrFDays, 1):

        if i == 0:
            payPerDay = payPerDay
        else:
            payPerDay += payPerDay
            
        payNDlrs = payPerDay/100
        totalPayNDlrs += payNDlrs
        print('Pay daily in dollars $%.2f' %payNDlrs)
        
    print('Total pay for the period $%.2f' %totalPayNDlrs)


main()
