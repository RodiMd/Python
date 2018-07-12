#Lottery Number Generator
#program to generate a seven digit number, random numbers
#0-9 and assign each to a list element.

import random

def main():
    lotList = [0, 0, 0, 0, 0, 0, 0]
    i = 0 #counter
    for i in range(0, 7):
        genLotNum = random.randint(0, 9)
        lotList[i] = genLotNum

    index = 0
    while index < len(lotList):
        lotList[index] = lotList[index]
        index +=1
    print(lotList)

main()
    
