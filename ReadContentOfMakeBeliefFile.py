#File Display
#assume file exists containing a series of integers, numbers.txt
#write a program that will display all of the file's contents

def main():
    #open a file
    file = open('numbers.txt', 'r')
    content = file.read()
    print(content)
    file.close()

main()
