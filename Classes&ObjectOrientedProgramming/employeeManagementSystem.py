#Employee Management System
#store employee objects in a dictionary
#use employee id as key
#present a menu to perform: lookup, add, change, delete, quit program

import employeeclass
import pickle

#create Global constants for menu choices

lookup = 1
add = 2
change = 3
delete = 4
QUIT = 5

fileName = 'employeesList.dat'

def main():

    employees = loadEmployees()
    choice = 0
    
    #Choose the action desired;
    while choice != QUIT:
        choice = get_menuChoice()
        if choice == lookup:
            lookUP(employees)
        elif choice == add:
            adD(employees)
        elif choice == change:
            changE(employees)
        elif choice == delete:
            deletE(employees)

    saveEmployeeList(employees)

def loadEmployees():
    try:
        inputFile = open(fileName, 'rb')
        employeeList = pickle.load(inputFile)
        inputFile.close()

    except IOError:
        employeeList = {}

    return employeeList

def get_menuChoice():
    print()
    print('Menu')
    print('---------------')
    print('1. Look up an employee ')
    print('2. Add and employee ')
    print('3. Change employee data ')
    print('4. Delete an employee data ')
    print('5. Quit the program ')
    print()

    choice = int(input('Enter a choice '))

    while choice < lookup or choice > QUIT:
        choice = int(input('Enter a valid choice: '))
        print('the choice is ', choice)

    return choice

def lookUP(employees):
    ID = input('Enter an ID ')
    print(employees.get(ID, 'The ID was not found'))
    
def adD(employees):
    name = input('name: ')
    ID = input('ID: ')
    Department = input('Department: ')
    jobTitle = input('Title: ')

    employeeInfo = employeeclass.Employee(name, ID, Department, jobTitle)

    if ID not in employees:
        employees[ID] = employeeInfo
        print('The entry has been added')
    else:
        print('The employee already exists')

def changE(employees):
    ID = input('Enter a name: ')
    if ID in employees:
        name = input('Enter a new name ')
        Department = input('Enter a new department ')
        jobTitle = input('Enter a new job title ')

        employeeInfo = employeeclass.Employee(name, ID, Department, jobTitle)
        emplyees[ID] = employeeInfo
        print('Info has been updated ')
    else:
        print('The ID was not found ')

def deletE(employees):
    ID = input('Enter the ID: ')
    if ID in employees:
        del employees[ID]
        print('Entry deleted ')
    else:
        print('The ID was not found ')

def saveEmployeeList(employees):
    outputFile = open(fileName, 'wb')
    pickle.dump(employees, outputFile)
    outputFile.close()

main()


    
