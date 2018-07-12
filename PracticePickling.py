#pickling

import pickle

def main():
    
    dictionary={'rodi':'rodi_murad@yahoo.com', 'olga':'olga15ua@gmail.com'}

    outputfile = open('pickledFile.dat', 'wb')
    pickle.dump(dictionary, outputfile)
    outputfile.close()

    inputFile = open('pickledFile.dat', 'rb')
    dictionary = pickle.load(inputFile)
    print(inputFile)
    inputFile.close()

main()
