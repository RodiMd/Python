#distance the object falls in a specific time using gravity
#d = 1/2 gt^2
#d - distance, g = 9.8, t - time in seconds.
#calls function in a loop (1,10)

gravity = 9.8
time = 0
distance = 0

def main():
    for time in range(1, 11):        
        distance = falling_distance(gravity, time)
        print('the distance is at time ', time, 'is %.2f '%distance)

    
def falling_distance(g, t):
    #return distance in meters
    distance = 0.5 * g * t**2
    return distance

main()
