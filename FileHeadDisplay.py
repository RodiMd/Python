#file head display
#ask user for a file name, display file contents, if less than five lines
# display all, if more than 5 lines display first five


def main():
    
      userEnt = input('Enter the file name ')
      file = open(userEnt, 'r')
      read = file.readline()
      print(read)
      count = 0
      while count < 4 and read != '':
          read = file.readline()
          print(read)
          count+=1
          
      file.close()

main()    
