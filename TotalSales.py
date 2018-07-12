#Total Sales

Week = ['Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def main():
    dailySales = open('dailySales.txt', 'w')
    
    for day in Week:
        print(day)
        sales = input('Enter sales for each day of the week ')
        dailySales.write(sales + '\n')
        
    dailySales.close()

    dailySales = open('dailySales.txt', 'r')
    readData = dailySales.readlines()
    dailySales.close()
    
    index = 0
    sumData = 0
    print(len(readData))
    
    while index < len(readData):
#since workin with lists and files, must use index
        readData[index] = int(readData[index])
        sumData += readData[index]
        index += 1
        
    print('Total sales for the weeks is ', sumData)

 # the routine below does not work with lists and files, while loop is more appropriate
 
##    sumData = 0
##    index = 0
##    qLines = len(readData)
##    for index in qLines:
##        readData[index] = int(readData[index])
##        sumData += readData[index]
##        index += 1
##
##    
##    print('Total sales for the weeks is ', sumData)
    
main()
