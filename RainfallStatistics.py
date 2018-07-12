#Rainfall Statistics
#user enter rainfall for each of the twelve months of the year
#calculate the total rainfall, the average and the max and min

def main():
    
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    monthlyRainfall = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count = 0
    cumulativeRainfall = 0
    rainfall = 0
    for count in range(0, 12):
        rainfall = input('Enter the rainfall for each month ' + months[count] + ': ')
        monthlyRainfall[count] = str(rainfall)
        cumulativeRainfall += int(rainfall)
        count += 1

    print(cumulativeRainfall)
    averageRainfall = cumulativeRainfall/count
    print(averageRainfall)

##    monthlyRainfall = float(monthlyRainfall)
    monthlyRainfall.sort() #this will sort smallest to largest 
    print(monthlyRainfall[11]) #choose max at the end of the list
    print(monthlyRainfall[0]) #choose min at beginning of the list
main()


    

    
