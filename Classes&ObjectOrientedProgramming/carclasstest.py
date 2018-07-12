#car class test


import carclass #import and the name of the module/file not the name of class in module

def main():

    year_model = input('Enter the year model of the car ')
    make = input('Enter the make of the car ')
    speed = 0
    accelerate = 5
    breakk = -5
    car = carclass.Car(year_model, make, speed, accelerate, breakk)

    speed = accelerating(car.get_accelerate(), car.get_speed())
    print('speed after accelerating ', speed)

    speed = breaking(car.get_breakk(), car.get_speed())
    print('speed after breaking ', speed)
def accelerating(accelerate, speed):
    
    for i in range (0, 5):        
        speed += accelerate
    return speed

def breaking(breakk, speed):
    
    for i in range(0, 5):
        speed += breakk
    return speed

main()
    
