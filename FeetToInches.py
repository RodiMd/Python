#Feet to Inches
#accept argument in feet and return value in inches

argInFeet = int(0)
foot_to_Inch = int (12)
feet = int(0)

def main():

    argInFeet = input('Enter a value in feet ')
    argInFeet = int(argInFeet)
    
#    totalInches = feet_to_inches(argInFeet)
    print(feet_to_inches(argInFeet))
    
#    print('The value in inches is ', totalInches)

def feet_to_inches (feet):
    return foot_to_Inch * feet
    
main()

#Note the results to this program initially multiplying 12in in a foot
# by an entry for argInFeet = 12, was getting an answer of 12121212---
# this type of result occurs when you multiply a string by a different
#type of value. so until I declared argInFeet = int
# i was getting the wring answer, now is good after declaring it to be
# a argInFeet = int(argInFeet)
