#Calories from fat and carbohydrates
#calories from fat = fat grams x 9
#calories from carbs = carb grams x 4

def fatNcarbCalories():
    fatGrams = input('Enter grams of fat consumed per day ')
    carbGrams = input('Enter grams of carb consumed per day ')
    
    caloriesFromFat = float(fatGrams) * 9.0
    caloriesFromCarbs = float(carbGrams) * 4.0
    print ('Total calories consumed from fat is %.2f' %caloriesFromFat)
    print ('Total calories consumed from carbs is %.2f' %caloriesFromCarbs)
    
    totalCalories = caloriesFromFat + caloriesFromCarbs
    print ('Total calories consumed daily is %.2f ' %totalCalories)
    
    
fatNcarbCalories()
