#word separator
#enter a sentence with all words not being separated except
#the first letter of each word is capitalized

def main():
    string = input('Enter a sentence witout spaces, just capitalize beginning of each word ')
    string2 = ''
    i = 0

    while i < len(string):
        #string2 += string[i]

        if i == 0:
            string2 += string[i]
            
        elif string[i].islower():
            string2 += string[i]

        elif string[i] == 'I':
            string2 += ' ' + string[i]

        elif string[i].isupper():
            string2 += ' ' + string[i].lower()

        i += 1

    print(string2)
main()
