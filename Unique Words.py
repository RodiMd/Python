#Unique Words
#record all words that have letter x and a in them.

def main():

    uniqueWords = open('UniqueWordsFile.txt','r')
    words = uniqueWords.readline()
    uWords = ''
    uWords2 = ''
    
    wordsList = ['']
    uniqueWords = ['']

    x = 0
    while x != len(words):
        uWords += words[x]
        x += 1

    y = uWords.count(' ')
    wordsList=[''] * (y+1) #makes the list 16 elements long
    print('length of words',len(words))
    i = 0
    j = 0
    for j in range(0,(len(words))):
        if uWords[j] != ' ':
            uWords2 += uWords[j] #uWords2 is used to record each word up to space


        elif uWords[j] == ' ':
            wordsList[i] = uWords2

            uWords2 = '' #when space is found, uWord2 is reset for next word after the space
            i+=1
# this if statement is used to account for the last word beyond the last space found
        if j == (len(words)-1):
            print(j)
            wordsList[i] = uWords2
            
    m = 0
    for k in range(0, len(wordsList)):
        if 'x' in wordsList[k] or 'a' in wordsList[k]:
            uniqueWords += ['']
            uniqueWords[m] = wordsList[k]
            m += 1
# this deletes any empty spaces created
    for k in range(0, len(uniqueWords)):
        if uniqueWords[k] == '':
            del uniqueWords[k]
    

    print(uWords)
    print(wordsList)
    print(uniqueWords)
main()
