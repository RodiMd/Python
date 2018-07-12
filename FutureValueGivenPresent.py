#Future Value
#earn compound monthly interest
#F=Px(1+i)^t
#F - future value of the account after specified time
#P - present value of the account
#i - monthley interest rate
#t - number of months
#prompt user to enter present value, monthly interest, number of months
#once all values entered, display the future value

future = float(0)
interest = float(0)
time = float(0)
present = float(0)

def main():
    present = input('Enter the present account value ')
    interest = input('Enter the monthly interest rate ')
    time = input('Enter the number of compounding time in months ')

    fValue = future_Value(present, interest, time)
    print ('The future value of the account is %.2f ' %fValue)
    
def future_Value(p, i, t):
    i = float(i)
    p = float(p)
    t = float(t)
    f = float(0.0)
    f = p * (1 + i)**t

    return f

main()
