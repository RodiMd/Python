#CapitalQuiz
import random

def main():

    states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii',
                'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
                'Missuri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersy', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
                'Oklahoma',' Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennesse', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
                'West Virginia', 'Wisconsin', 'Wyoming']
                
    capitalsUS = {'Alabama':'Montgomery', 'Alaska':'Juneau', 'Arizona':'Phoenix', 'Arkansas':'Little Rock', 'California':'Sacramento',
                  'Colorado':'Denver', 'Connecticut':'Hartford', 'Delaware':'Dover', 'Florida':'Tallahassee', 'Georgia':'Atlanta',
                  'Hawaii':'Honolulu', 'Idaho':'Boise', 'Illinois':'SpringField', 'Indiana':'Indianapolis', 'Iowa':'Kansas',
                  'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge', 'Maine':'Augusta', 'Maryland':'Annapolis', 'Massachusetts':'Boston',
                  'Michigan':'Lansing', 'Minnesota':'Saint Paul', 'Mississippi':'Jackson', 'Missouri':'Jefferson City', 'Montana':'Helena',
                  'Nebraska':'Lincoln', 'Nevada':'Carson City', 'New Hampshire':'Concord', 'New Jersey':'Trenton', 'New Mexico':'Santa Fe',
                  'New York':'Albany', 'North Carolina':'Raleigh', 'North Dakota':'Bismarck', 'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                  'Oregon':'Salem', 'Pennsylvania':'Harrisburg', 'Rhode Island':'Providence', 'South Carolina':'Columbia', 'South Dakota':'Pierre',
                  'Tennessee':'Nashville', 'Texas':'Austin', 'Utah':'Salt Lake City', 'Vermont':'Montpelier', 'Virginia':'Richmond', 'Washington':'Olympia',
                  'West Virginia':'Charleston', 'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

    count = 0 #counter for correct reponses
    count2 = 0 #counter for incorrect reponses
    yn = 'y'
    
    while yn == 'y':

        x = random.randint(0,49)
        print(x)        
        print('What is the capital of ', states[x])
        capital = input('Enter the capital of '+states[x]+ ': ')
        cpl = capital[0].upper() #to make first letter upper case
        
        for i in range(1, len(capital)):
            cpl += capital[i]
        print(cpl)

#        print(states[x])
        y =''
        y = states[x] #could not put states[x] as the key, the dictionary wasnt reading it.
        if cpl != '' and cpl == capitalsUS[y]:
            print('Your response is correct!')
            count += 1
            yn = input('Would you like to continue, y/n? ' ).lower()
        elif cpl != '' and cpl != capitalsUS[y]:
            print('Your reponse is incorrect!'+ ' The correct response is: '+ capitalsUS[y])
            count2 += 1
            yn = input('Would you like ot continue, y/n? ').lower()
            
        
    print('correct answers ', count, 'incorrect answers ',count2)
main()
