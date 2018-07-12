#Automobile Costs
#ask user to input automobile costs including: loan payment
#insurance, gas, oil, tires, maintenance.

loanPayment = input('Enter auto monthly payment ')
insurance = input('Enter insurance cost ')
gas = input('Enter monthly gas cost ')
oil = input('Enter monthly oil cost ')
tires = input('Enter montly tires cost ')
maintenance = input('Enter monthly maintenance cost ')
oil = (1.0 / 3.0) * float(oil)
tires = (1.0 / 24.0) * float(tires)

def main():
    totalMonthlyCost = float(loanPayment) + float(insurance) + float(gas) + float(oil) + float(tires)
    + float(maintenance)
    print ('Total monthly cost of a car %.2f ' %totalMonthlyCost)

main()
