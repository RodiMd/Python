#Sentence Capitalizer

def main():

    userInput = input('Enter a sentence ')
    userOutput = ''
          
    for i in range(0,len(userInput)):
        
        if i == 0:
            userOutput += userInput[i].upper()
            
        elif i == len(userInput):
            print(userOutput)
            
        elif userInput[i - 2] == '.' and i < (len(userInput) - 2):
            userOutput += userInput[i].upper()
            
        elif userInput[i - 2] == '?' and i < (len(userInput) - 2):
            userOutput += userInput[i].upper()

        elif userInput[i - 2] == '!' and i < (len(userInput) - 2):
            userOutput += userInput[i].upper()

        else:
            userOutput += userInput[i]
        
        
    print(userOutput)

main()
