#Word Frequency

def main():

    quantityWords = open('UniqueWordsFile.txt', 'r')
    count = quantityWords.readline()
    keyWordDictionary = {}
    keyWordList = ['']
    print(count)

    #routine to detect all spaces, once detected register the word and place it
    #in dictionary
    i = 0
    j = 0 #counter for statement
    keyWord = ''
    y = count.count(' ')
    keyWordList = ['']*(y+1)
  
    while count != '' and i < len(count):
        keyWord += count[i]
        if count[i] == ' ':
            keyWordList[j] = keyWord
            j += 1
            keyWordDictionary[keyWord] = 1
            keyWord = ''
        i += 1
        
# this is used to delete any empty elements in the list
    for i in range(0, len(keyWordList)):
        if keyWordList[i] == '':
            del keyWordList[i]
    print(keyWordList)
    print()

# this routing is to count the numbe of occurence of a word. if more than once
# then record it.
    for i in range(0, len(keyWordList)):
        x = keyWordList.count(keyWordList[i])
        if x > 1:
            keyWordDictionary[keyWordList[i]] = x

    print(keyWordDictionary)
main()
# routine to find the words that occur more than once and count the number of times they occur
##    countWords = 1
##    k = 0
##    l = k + 1
##    while k < len(keyWordList):
##        while l < len(keyWordList):
##            if keyWordList[k] == keyWordList[l]:
##                countWords += 1
##                keyWordDictionary[keyWordList[k]] = countWords
##                print(k, l, countWords, keyWordList[k], keyWordList[l])
##                
##            l += 1
##        countWords = 1
##        k += 1
##        l  = k + 1
##    print(keyWordDictionary)                
    


