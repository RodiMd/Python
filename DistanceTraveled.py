#Distance traveled
#distance = speed x time
#40mph for 3hrs, distance travelled in 120min

speed = input('Enter your speed in mph ')
speed = int(speed)
hrsDriven = input('Enter the number of hours driven ')
hrsDriven = int(hrsDriven)
i = 0

def main():
        print('Hour\t\tDistance Traveled ')
        global hrsDriven
        for i in range(1, hrsDriven+1, 1):
            distanceTraveled = speed * i
            print(i, '\t\t\t', distanceTraveled)
            
main()
