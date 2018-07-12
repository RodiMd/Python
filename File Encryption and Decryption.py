#File Encryption and Decryption
#use dictionary to assign codes to each letter of the alphabet

def main():

    codes = {'A':'!', 'a':'0', 'B':'@', 'b':'9', 'C':'#', 'c':'8', 'D':'$',
             'd':'7', 'E':'%', 'e':'6', 'F':'^', 'f':'5', 'G':'&', 'g':'4',
             'H':'*', 'h':'3', 'I':';;', 'i':'2', 'J':'~', 'j':'1', 'K':'x',
             'k':'?', 'L':'b', 'l':'Y', 'M':'e', 'm':'q', 'N':'a', 'n':'c',
             'O':'f', 'o':'D', 'P':'j', 'p':'G', 'Q':'B', 'q':'J', 'R':'K',
             'r':'E', 'S':'A', 's':'d', 'T': 'I', 't':'L', 'U':'C', 'u':'>',
             'V':'<', 'v':'/', 'W':'F', 'w':'k', 'X':'r', 'x':'R', 'Y':'t',
             'y':'o','Z':'n', 'z':'s', ' ': '-'}

    cipherList = ''
    cipher = open('cipherFile.txt', 'r')
    content = cipher.readline()
    print(content)
    
    i = 0
    while content != '' and i < len(content):
        if content[i] in codes:
            x = content[i]
            cipherList += codes[x]
            
        elif content[i] == ' ':
            cipherList += ' '
            
        i += 1
    cipher.close()
    #write to file encrypted text file
    cipher2 = open('cipherFileWritten.txt', 'w')
    for i in range(0, len(cipherList)):
        cipher2.write(cipherList[i])
        
    cipher2.close()
    #read the encrypted text file
    cipherRead = open('cipherFileWritten.txt', 'r')
    cipherReadContent = cipherRead.readline()
    print(cipherReadContent)
    cipherRead.close()
    
main()
    

