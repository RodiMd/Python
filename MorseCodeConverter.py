#Morse Code Converter
#in this code each letter, digit and punctuation characters are
#represented by dots and dashes.
#write a program that asks the user to enter a string then convert to Morse code

def main():

    characters = [' ', ',','.','?','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    code = [' ', '--..--', '.-.-.-', '..--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '----.', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.-', '--..']

    userInput = input('Enter a string of characters ')
    codedInput = [0] * len(userInput)
    
    for i in range(0, len(userInput)):
        for j in range(0, len(characters)):

            if userInput[i] == characters[j]:
                codedInput[i] = code[j]
            
    print(codedInput)
    
main()
        
