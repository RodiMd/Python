#main method to call class

import classmodule

def main():

    x = int(input('Enter a value for x '))
    y = int(input('Enter a value for y '))
    
#passes the values to the module
    variables = classmodule.Calculate(x, y)
    
#gets the values from module and performs calculations    
    z = variables.get_x() * variables.get_y()
    print(z)

#passes the x and y variables to the division function
    div = division(variables.get_x(), variables.get_y())
    print(div)

def division(x, y):

    div = x/y
    return div
main()
    
    
