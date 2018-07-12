#BMI calculator
#BMI = weight x 703/height^2
#weight is entered in pounds and height in inches
# ** - is used instead of using ^

weight = input('Enter your weight ')
height = input('Enter your height ')

def BMI():
    BMI = float(weight) * 703.0/(float(height))**2
    print ('Your BMI is %.2f' %BMI)

BMI()
