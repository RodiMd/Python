#Body mass index
#height in inches, weight in pounds
# bmi = weight x 703/height^2

weight = input('Enter your weight ')
height = input('Enter you height ')
weight = float(weight)
height = float(height)

def main():
    bmi = weight * 703/(height**2)
    if bmi < 18.5:
        print ('Your BMI is %.2f ' %bmi, 'you are underweight ')
    elif bmi >= 18.5 and bmi <= 25:
        print ('Your BMI is %.2f ' %bmi, ',you have the optimal weight ')
    else:
        if bmi > 25:
            print('Your BMI is %.2f ' %bmi, 'you are overweight ')
main()
    
