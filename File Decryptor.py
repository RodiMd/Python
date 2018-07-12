#File Decryption

def main():

    codes = {'!':'A', '0':'a', '@':'B', '9':'b', '#':'C', '8':'c', '$':'D',
             '7':'d', '%':'E', '6':'e', '^':'F', '5':'f', '&':'G', '4':'g',
             '*':'H', '3':'h', ';;':'I', '2':'i', '~':'J', '1':'j', 'x':'K',
             '?':'k', 'b':'L', 'l':'Y', 'e':'M', 'q':'m', 'a':'N', 'c':'n',
             'f':'O', 'D':'o', 'j':'P', 'G':'p', 'B':'Q', 'J':'q', 'K':'R',
             'E':'r', 'A':'S', 'd':'s', 'I':'T', 'L':'t', 'C':'U', '>':'u',
             '<':'V', '/':'v', 'F':'W', 'k':'w', 'r':'X', 'R':'x', 't':'Y',
             'o':'y', 'n':'Z', 's':'z', '-':' '}

    cipherList = ''
    cipher = open('cipherFileWritten.txt', 'r')
    content = cipher.readline()
    print(content)

    i = 0
    while content != 0 and i < len(content):
        if content[i] in codes:
            x = content[i]
            cipherList += codes[x]
        i += 1

    cipher.close()

    cipher2 = open('decryptedFileWritten.txt', 'w')
    cipher2.write(cipherList)
    cipher2.close()

    cipher2 = open('decryptedFileWritten.txt', 'r')
    content = cipher2.readline()
    cipher2.close()

    print(content)

main()
