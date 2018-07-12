#File Analysis
#compare two files:
#unique words,
#similar words
#words found in one but not the other
#words found in the second but not the first
#different words that appear in one or ther other but not both
#HINT: set operations to perform the analyses

def main():
    uniqueWordFile = open('UniqueWordsFile.txt', 'r')
    readUniqueWordsFile = uniqueWordFile.read()
    uniqueWords = ''
    uniqueWordFileSet = set()
    
    i = 0
    while readUniqueWordsFile != '' and i < len(readUniqueWordsFile):
        uniqueWords += readUniqueWordsFile[i]

        if readUniqueWordsFile[i] == ', ' or readUniqueWordsFile[i] == ' ' or readUniqueWordsFile[i] == '. ' or readUniqueWordsFile[i] == '\n':
            
            if ', ' in uniqueWords:
                uniqueWords = uniqueWords[:-2]
                uniqueWords += ' '
                
            elif '. ' in uniqueWords:
                uniqueWords = uniqueWords[:-1]
                uniqueWords += ' '
                
            elif '\n' in uniqueWords:
                uniqueWords = uniqueWords[:-1]
                uniqueWords += ' '
                
            uniqueWordFileSet.add(uniqueWords)
            uniqueWords = ''
        i += 1
    if '' in uniqueWordFileSet:
        uniqueWordFileSet.remove('')
    elif ' ' in uniqueWordFileSet:
        uniqueWordFileSet.remove(' ')
    
    print('-------')
    print(uniqueWordFileSet)
#routine  to make a set containing the cipher text file

    cipherFile = open('cipherFile.txt', 'r')
    readCipherFile = cipherFile.read()
    cipherWords = ''
    cipherWordsFileSet = set()
    
    k = 0
    while readCipherFile != '' and k < len(readCipherFile) :
        cipherWords += readCipherFile[k]

        if readCipherFile[k] == ', ' or readCipherFile[k] == ' ' or readCipherFile[k] == '.' or readCipherFile[k] == '\n':

            if ',' in cipherWords:
                cipherWords = cipherWords[:-2]
                cipherWords += ' '
                
            elif '.' in cipherWords:
                cipherWords = cipherWords[:-1]
                cipherWords += ' '
                
            elif '\n' in cipherWords:
                cipherWords = cipherWords[:-1]
                cipherWords += ' '

            cipherWordsFileSet.add(cipherWords)
            cipherWords = ''

        k += 1
    if '' in cipherWordsFileSet:
        cipherWordsFileSet.remove('')
    elif ' ' in cipherWordsFileSet:
        cipherWordsFileSet.remove(' ')
        
    print('-----------------')
    print(cipherWordsFileSet)

# look for similar words

    unionTextFiles = uniqueWordFileSet.intersection(cipherWordsFileSet)
    print('----INTERSECTION----')
    print(unionTextFiles)

# look for words found in unique words list and not in cipher words list
    firstNotSecond = uniqueWordFileSet.difference(cipherWordsFileSet)
    print('----DIFFERENCE----')
    print(firstNotSecond)

# look for words found in cipher Words List and not in Unique Words
    secondNotFirst = cipherWordsFileSet.difference(uniqueWordFileSet)
    print('----DIFFERENCE2----')
    print(secondNotFirst)

# This should be the union of both differences
    unionOfTwoDifferences = secondNotFirst.union(firstNotSecond)
    print('----UNIONOFDIFFERENCE----')
    print(unionOfTwoDifferences)

main()













#The below code, takes two files and creates two lists. I though i can create a list
# and from the list create a set, but I wasnt able to convert a list into a set.

##def main():
##
##    uniqueWordsFile = open('UniqueWordsFile.txt', 'r')
##    readUniqueWordsFile = uniqueWordsFile.read()
##
###making the file text contents into a list of words first
##    uniqueWordsFileList = ['']
##    uniqueWords = ''
##
##    i = 0
##    j = 0
##    while readUniqueWordsFile != '' and i < len(readUniqueWordsFile):
##        uniqueWords += readUniqueWordsFile[i]
##        
##        if readUniqueWordsFile[i] == ', ' or readUniqueWordsFile[i] == ' ' or readUniqueWordsFile[i] == '.' or readUniqueWordsFile[i] == '\n':
##            #the next two lines used to ensure that comma doesnt get added to variable
##            uniqueWordsFileList += ['']
##            
##            if ',' in uniqueWords:
##                uniqueWords = uniqueWords[:-2]
##                uniqueWords += ' '
##                
##            elif '.' in uniqueWords:
##                uniqueWords = uniqueWords[:-1]
##                uniqueWords += ' '
##                
##            elif '\n' in uniqueWords:
##                uniqueWords = uniqueWords[:-1]
##                uniqueWords += ' '
##
##            uniqueWordsFileList[j] = uniqueWords
##            uniqueWords = ''
##            j += 1
##        i += 1
##        
##    i = 0
##    while uniqueWordsFileList != '' and i < len(uniqueWordsFileList):
##        if uniqueWordsFileList[i] == '' or uniqueWordsFileList[i] == ' ':
##                del uniqueWordsFileList[i]
##        i += 1
##
##    print(uniqueWordsFileList)
##    uniqueWordsFile.close()
##
##
##    cipherFile = open('cipherFile.txt', 'r')
##    readCipherFile = cipherFile.read()
##
##    cipherWordsFileList = ['']
##    cipherWords = ''
##    k = 0
##    l = 0
##    while readCipherFile != '' and k < len(readCipherFile) :
##        cipherWords += readCipherFile[k]
##
##        if readCipherFile[k] == ', ' or readCipherFile[k] == ' ' or readCipherFile[k] == '.' or readCipherFile[k] == '\n':
##            #the next two lines used to ensure that comma doesnt get added to variable
##            cipherWordsFileList += ['']
##
##            if ',' in cipherWords:
##                cipherWords = cipherWords[:-2]
##                cipherWords += ' '
##                
##            elif '.' in cipherWords:
##                cipherWords = cipherWords[:-1]
##                cipherWords += ' '
##                
##            elif '\n' in cipherWords:
##                cipherWords = cipherWords[:-1]
##                cipherWords += ' '
##
##            cipherWordsFileList[l] = cipherWords
##            cipherWords = ''
##            l += 1
##        k += 1
##    i = 0
##    while cipherWordsFileList != '' and i < len(cipherWordsFileList):
##        if cipherWordsFileList[i] == '' or cipherWordsFileList[i] == ' ':
##                del cipherWordsFileList[i]
##        i += 1
##        
##    print('-----------------')
##    print(cipherWordsFileList)
##
##    # now that both files are converted to lists of words, we will create sets containing the words
##        
##
##    myUniqueWordsFileSet = set(uniqueWordsFileList)
##    myCipherFileSet = set(cipherFileList)
##
##    print(myUniquesWordsFileSet)
##    print('-----')
##    print(myCipherFileSet)
##    
##main()
