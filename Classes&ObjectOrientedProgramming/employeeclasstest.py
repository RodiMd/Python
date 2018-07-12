#Employee class test

import employeeclass #import the employee class module

def main():

    accountingList = employeeEntryAccounting() #call the accounting method
    itList = employeeEntryIT()
    manufacturingList = employeeEntryManufacturing()
    
    displayList(accountingList, itList, manufacturingList)

def employeeEntryAccounting():

    accountingList = []#create an empty list 
    quantityOfInput = input('How many employees in Accounting would you like to enter? ')
    #iterate through the number of employees desired to be registered
    for i in range (0, int(quantityOfInput)):
        Name = input('Enter the name of the employee ')
        ID_number = input('Enter the id number of the employee ')
        Department = input('Enter the department in which the employee works ')
        Job_title = input('Enter the job title of the employee ')
        print('')
        #pass entered data to be initialized and set in the module
        info = employeeclass.Employee(Name, ID_number, Department, Job_title)
        #accept various ways to typing the department
        if Department == 'accounting' or 'Accounting' or 'ACCOUNTING':
            Department = Accounting #keep consistency in name of the department
            accList = employeeclass.Employee(Name, ID_number, Department, Job_title)
            accountingList.append(accList) #add data to the list
    return accountingList

def employeeEntryIT():
    itList = []
    quantityOfInput = input('How many employees in IT would like to enter? ')

    for i in range (0, int(quantityOfInput)):
        Name = input('Enter the name of the employee ')
        ID_number = input('Enter the id number of the employee ')
        Department = input('Enter the department in which the employee works ')
        Job_title = input('Enter the job title of the employee ')
        print('')
        info = employeeclass.Employee(Name, ID_number, Department, Job_title)
        
        if Department == 'IT' or 'it' or 'It' or 'iT':
            Department = IT
            it_list = employeeclass.Employee(Name, ID_number, Department, Job_title)
            itList.append(it_list)
    return itList
        
def employeeEntryManufacturing():
    manufacturingList = []
    quantityOfInput = input('How many employees in Manufacturing would you like to enter? ')
    i = 1

    for i in range (0, int(quantityOfInput)):
        Name = input('Enter the name of the employee ')
        ID_number = input('Enter the id number of the employee ')
        Department = input('Enter the department in which the employee works ')
        Job_title = input('Enter the job title of the employee ')
        print('')
        info = employeeclass.Employee(Name, ID_number, Department, Job_title)

        if Department == 'Manufacturing' or 'manufacturing' or 'MANUFACTURING':
            Department = Manufacturing
            manu_List = employeeclass.Employee(Name, ID_number, Department, Job_title)
            manufacturingList.append(manu_List)
    return manufacturingList
        
def displayList(accountingList, itList, manufacturingList):

    for item in accountingList:
        print('The name of the employee ', item.get_Name())
        print('The employee\'s id number is ', item.get_ID_number())
        print('The employee\'s Department ', item.get_Department())
        print('The employee\'s title ', item.get_Job_title())
        print('---------------------------------')

    for item in itList:
        print('The name of the employee ', item.get_Name())
        print('The employee\'s id number is ', item.get_ID_number())
        print('The employee\'s Department ', item.get_Department())
        print('The employee\'s title ', item.get_Job_title())
        print('---------------------------------')

    for item in manufacturingList:
        print('The name of the employee ', item.get_Name())
        print('The employee\'s id number is ', item.get_ID_number())
        print('The employee\'s Department ', item.get_Department())
        print('The employee\'s title ', item.get_Job_title())
        print('---------------------------------')

main()
