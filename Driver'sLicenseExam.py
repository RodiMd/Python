#Driver's License Exam
#20 multiple choice questions
#correct answers:a,c,a,a,d,b,c,a,c,b,a,d,c,a,d,c,b,b,d,a
#store correct answers in a list, read student's answer and store
#the answers in a another list, create text file to test app
#message (pass or fail), correctly answer 15/20, then display the
#correct answers, number of incorrectly answered questions, and question numbers

def main():
    try:
        correctAnswers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
#       questionNumber = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
        questionNumber = [0] * 20
        studentAnswerList = [0] * 20
        count = 0
        
        studentAnswers = open('studentAnswers.txt', 'w')#create txt file to hold student's answers
        
        for i in range(0,20):
            questionNumber[i] = i+1

        for j in range(0,20):
            questionNumber[j] = str(questionNumber[j])
        #allow student to input the answers believed to be true and writes answers to text flle
        while count < len(correctAnswers):
            studentInput = input('Enter the Answer for question '+ questionNumber[count] + ' ')
            studentInput = str(studentInput)
            studentAnswers.write(studentInput + '\n')
            count+=1
        studentAnswers.close()

        studentAnswers = open('studentAnswers.txt', 'r')
        studentAnswerList = studentAnswers.readlines()
        #routine to strip away the \n from each interested line of code
        index = 0
        while index < len(studentAnswerList):
            studentAnswerList[index] = studentAnswerList[index].rstrip('\n')
            index += 1
            
#        print(studentAnswerList)
        studentAnswers.close()

        #routing to compare list contents
        count = 0
        correct = 0
        incorrect = 0
        incorrectAnswers = [0] * 20
        for count in range(0, 20):
            if studentAnswerList[count] == correctAnswers[count]:
                correct += 1
            elif studentAnswerList[count] != correctAnswers[count]:
                incorrect += 1
                incorrectAnswers[count] = studentAnswerList[count]
        print(studentAnswerList)
        print(correctAnswers)

        #if statement to compare answers and indicate if student passed or failed
        if correct >= 15:
            print('Passed ', correct)
        else:
            print('Failed ', incorrect)
        print (incorrectAnswers)
    except IndexError:
        print('Went out of range')

main()

