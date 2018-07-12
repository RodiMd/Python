#Time calculator

timeNSecnds = input('Enter a number of seconds ')
timeNSecnds = float(timeNSecnds)

def main():
    
    if  timeNSecnds >= 60 and timeNSecnds < 3600:
        rmndrScnds = timeNSecnds % 60
        print('remainder of seconds are ',rmndrScnds)
        timeNsecnds = timeNSecnds - rmndrScnds
        print('time in seconds is ',timeNsecnds)
        timeNmnts = timeNsecnds / 60
        print('The number of minutes in the entered is %.2f ' %timeNmnts)
        
    elif timeNSecnds >= 3600 and timeNSecnds < 86400:
        rmndrScnds = timeNSecnds % 3600
        print('remainder seconds are', rmndrScnds)
        timeNsecnds = timeNSecnds - rmndrScnds
        print('time in seconds is ', timeNsecnds)
        timeNHrs = timeNsecnds / 3600
        print('The number of hours in the entered is %.2f ' %timeNHrs)
        timeNmnts = rmndrScnds / 60
        print('The number of minutes in the entered is %.2f ' %timeNmnts)
        
    elif timeNSecnds >= 86400:
        rmndrScnds = timeNSecnds %3600
        print('remainder of seconds are ', rmndrScnds)
        timeNsecnds = timeNSecnds - rmndrScnds
        print('time in seconds is ', timeNsecnds)
        timeNDays = timeNsecnds / 86400
        print('The number of days in the entered is %.2f ' %timeNDays)
        
    else:
        print('Enter a valid number')

main()
