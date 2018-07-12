#Date Printer

def main():

    date = input('Enter a date in a form of e.g. mm/dd/yyyy ')

    newDate = date.split('/')
    print(newDate)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    fC = int(newDate[1]) #fC - firstCharacter in the newDate
    
    print(months[fC], ' ', newDate[1], ', ', newDate[2] )
    
main()
