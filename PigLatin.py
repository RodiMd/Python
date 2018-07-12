#Pig Latin
#accept sentence as input, and convert to PigLatin

def main():

    englishString = input('Enter a sentence ')
    latinString = [''] * len(englishString)
    latinString2 = ''
    
    latinString = englishString.split(' ')
    x = ''
    print(latinString)   
    
    j = 0
    for i in range(0, len(latinString)):
        y = len(latinString[i]) #takes the length of the list element for each i
        variable = '' #remove the previous content of the variable element to record new
        for j in range(0, len(latinString[i]), y):
            
            x = latinString[i][0] + 'AY '
            print(i,'& ', j, '&', len(latinString[i]), '&', x, '&', y)

            #this for loop variable is need to delete the first item of each element
            #from the latinString list
            for k in range(1, len(latinString[i])):
                variable += latinString[i][k]

            #creates a latinString2 that contains all the element form teh latinString list
            latinString2 += variable + x
    
    print(latinString2)

main()
    
