#The most frequent character

def main():

    string = input('Enter a string to find the most frequent character ')
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    string2 = string.lower()
    counter = [''] * len(alphabet)
    equalCharacters = [''] 
    
    count = 0
    count2 = 0
    j = 0

    #the following for loop is used to compare values between the alphabet and the entered string
    for i in range(0, len(alphabet)):
        while j < len(string2):
            if alphabet[i] == string2[j]:
                count += 1
            j += 1
        counter[i] = count #counter at position i takes the number of times the same letter was encountered
        count = 0
        j = 0
    print(counter)

    #the following while statement goes through the counter list and checks for the highest value
    k = 0
    l = 1
    while k <(len(counter)) and l < (len(counter)):
        if counter[k] > counter[l]:
            l += 1
            
        elif counter[k] < counter[l]:
            k = l
            l += 1
            
        elif counter[k] == counter[l]:
            l += 1
            
        if l == len(counter):
            print('The most fequently encountered letter is ', alphabet[k], 'and it is found ', counter[k], 'times')
#check back to this program        

main()
