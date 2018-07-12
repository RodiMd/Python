#Line numbers

def main():
    fileName = input('Enter the name of the file ')
    fileName = open(fileName, 'r')
    readL = fileName.readline()
    count = 2
    print('1 : ', readL)
    while readL != '':
        readL = fileName.readline()
        if readL != '':
            print(count,': ', readL)
            count+=1
            
    fileName.close()
main()
