#Item counter

def main():

    myFile = open('file.txt', 'r')
    read = myFile.readline()
    
    if read != '':
        count =1
    else:
        count = 0
        
    while read != '':
        read = myFile.readline()
        if read != '':
            count+= 1
    print (count)
    myFile.close()
main()
