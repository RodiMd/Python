#Stadium Seating
#class A seats cost $15, class B $12, cloass C $9

classATickets = input('Enter the quantity of Class A tickets purchased ')
classBTickets = input('Enter the quantity of Class B tickets purchased ')
classCTickets = input('Enter the quantity of Class C tickets purchased ')

classATickets = float(classATickets)
classBTickets = float(classBTickets)
classCTickets = float(classCTickets)

def revenue():
    totalRevenueA = classATickets * 15.0
    totalRevenueB = classBTickets * 12.0
    totalRevenueC = classCTickets * 9.0
    totalRevenue = totalRevenueA + totalRevenueB + totalRevenueC
    print ('Total Revenue %.2f' %totalRevenue)

revenue()
