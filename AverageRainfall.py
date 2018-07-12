#Average Rainfall
#nested loops to collect and calculate average rainfall
#over a period of years
#inner loop will iterate twelve times every month, each
#iteration will ask the user for inches of rainfall for the month
#after all iterations the program should display all months
#total inches of rainfall and the average rainfall per month for the entire period

def main():
# first loop for a period of years
# second loop for a period of months

    yearsInpt =  input('Enter the number of years you wish to enter rainfall data ')
    yearsInpt = int(yearsInpt)
    total = 0
    months = 12

    for i in range(0, yearsInpt):

        jan = int(input('Enter rainfall data in inches for the month of January '))
        feb = int(input('Enter rainfall data in inches for the month of February '))
        mar = int(input('Enter rainfall data in inches for the month of March '))
        apr = int(input('Enter rainfall data in inches for the month of April '))
        may = int(input('Enter rainfall data in inches for the month of May '))
        jun = int(input('Enter rainfall data in inches for the month of June '))
        jul = int(input('Enter rainfall data in inches for the month of July '))
        aug = int(input('Enter rainfall data in inches for the month of August '))
        sept = int(input('Enter rainfall data in inches for the month of September '))
        octbr = int(input('Enter rainfall data in inches for the month of October '))
        nov = int(input('Enter rainfall data in inches for the month of November '))
        dec = int(input('Enter rainfall data in inches for the month of December '))

        total += jan + feb + mar + apr + may + jun + jul + aug + sept + octbr + nov + dec

    totalMonths = months * yearsInpt
    print('total ',total, 'total months', totalMonths)
    averageRainfall = total / totalMonths
    print('years input ',yearsInpt)
    print('The avarage Rain fall for the specified period is %.2f' %averageRainfall)                    

main()
