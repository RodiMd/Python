#Test Average & Grade
#user enter five test scores
#display the letter grade for each score & then average all
# have to think about this program using loops

#this code works
##score1 = int(0)
##score2 = 0
##score3 = 0
##score4 = 0
##score5 = 0
##sc1 = int(0)
##sc2 = int(0)
##sc3 = int(0)
##sc4 = int(0)
##sc5 = int(0)


def main():

    score1 = input('Enter your grade ')
    score2 = input('Enter your grade ')
    score3 = input('Enter your grade ')
    score4 = input('Enter your grade ')
    score5 = input('Enter your grade ')

    print ('Score \t\t Grade ')
    print ('-----------------------')
    
    grades1 = determine_grade(score1)
    print (score1, '\t\t ', grades1)
    grades2 = determine_grade(score2)
    print (score2, '\t\t ', grades2)
    grades3 = determine_grade(score3)
    print (score3, '\t\t ', grades3)
    grades4 = determine_grade(score4)
    print (score4, '\t\t ', grades4)
    grades5 = determine_grade(score5)
    print (score5, '\t\t ', grades5)
    
    averages = avg_Grade(score1, score2, score3, score4, score5)
    print('The average score is %.2f '%averages)

def avg_Grade(s1, s2, s3, s4, s5):
    s1=int(s1)
    s2=int(s2)
    s3=int(s3)
    s4=int(s4)
    s5=int(s5)
    sumS = s1+s2+s3+s4+s5
    print(sumS)
    avg = sumS/5
    return avg
    
##def avg_grade (sc1, sc2, sc3, sc4, sc5):
##    sumScores = 0
##    sumScores = (sc1 + sc2 + sc3 + sc4 + sc5)
##    print (sumScores)
##    average = sumScores / 5
##    return average

def determine_grade(testScore):
    testScore = int(testScore)
    if testScore >= 90:
        grade = str('A')
    elif testScore >= 80 and testScore <90:
        grade = str('B')
    elif testScore >= 70 and testScore <80:
        grade = str('C')
    elif testScore >= 60 and testScore <70:
        grade = str('D')
    else:
        grade = str('F')
    return grade

main()

##    grades = calc_grades(s1, s2, s3, s4, s5)
##    print = (s1, s2, s3, s4, s5)
##
##def calc_grades(g1, g2, g3, g4, g5):
##    
##    g1 = int(input('Enter your grade '))
##    g2 = int(input('Enter your grade '))
##    g3 = int(input('Enter your grade '))
##    g4 = int(input('Enter your grade '))
##    g5 = int(input('Enter your grade '))
##
##    print ('Score\t\t Letter Grade')
##    print ('-------------------------------')
##
##    if g1 >= 90:
##        print (g1,'\t\t A')
##    elif g1 >= 80 and g1 < 90:
##        print (g1,'\t\t B')
##    elif g1 >= (g1, 
##
##    average = avg_grade(g1, g2, g3, g4, g5)
##    print(average)
##
##def avg_grade (sc1, sc2, sc3, sc4, sc5):
##    average = (sc1 + sc2 + sc3 + sc4 + sc5)/5
##    return average
##
##
##main()

#lets try this code

##grader = 0
##
##print ('Score \t\t Grade ')
##print ('-----------------------')
##
##def main():
##    
##    for i in range(5):
##        grade = input('Enter a grade ')
##
##        if grade >= 90:
##            print ('\t\t\t A')
##        elif grade >= 80 and grade < 90:
##            print ('\t\t\t B')
##        elif grade >= 70 and grade < 80:
##            print ('\t\t\t C')
##        elif grade >= 60 and grade < 70:
##            print ('\t\t\t D')
##        else:
##            print ('\t\t\t F')
##        
##        
##        
##                  
##
##
##    
##    
##main()

    
