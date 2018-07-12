#Budget Analysis
# enter amount budgeted for a month
# enter each expense and keep a running total
# display over or under budget


def main():

    amntBudgetedFor = input('Enter the amount budgeted for this month ')
    amntBudgetedFor = float(amntBudgetedFor)
    moreInpt = 'y'
    totalExpense = 0
    
    while moreInpt == 'y':
        global totalExpense
        moreInpt = input('Do you have expenses to Enter? ')
        if moreInpt == 'y':
            expenses = input('Enter monthly expenses you have ')
            expenses = float(expenses)
            totalExpense = float(totalExpense)
            totalExpense += expenses
        else:
            totalExpense = float(totalExpense)
            totalExpense += expenses

    total = amntBudgetedFor - totalExpense
    print ('The total saving/loss monthly is %.2f' %total)

main()
