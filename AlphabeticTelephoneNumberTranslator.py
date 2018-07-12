#Alphabetic Telephone Number Translator

def main():
    alphabet = ['-','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numerals = ['-',2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
    
    phoneNumber = input('Enter a phone number xxx-xxx-xxxx ')
    phoneNumber = phoneNumber.lower()
    enteredNumber = ''
    
    for i in range(len(phoneNumber)):
        if phoneNumber[i].isalpha():
            for j in range(len(alphabet)):
                if phoneNumber[i] == alphabet[j]:
                    enteredNumber += str(numerals[j])
        elif phoneNumber[i].isdigit():
            enteredNumber+= phoneNumber[i]
        else:
            enteredNumber += phoneNumber[i]

    print(enteredNumber)       

main()


        
