#Vowels and Consonants

def main():

    string = input('Enter a string to cound the vowels ')

    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    strg = ''
    
    for i in range(0, len(vowel)):
        if vowel[i] in string:
            count += 1
            strg += vowel[i] + ','

    print(count,'-', strg)
main()
