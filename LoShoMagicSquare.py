#Lo Shu Magic Square
#3x3 grid, contains numbers 1-9, the sum of each row, column and diagonal will add up equally
import random

def main():
    rowList = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0] ]
    i = 0
    j = 0
    for i in range(1,3):
        for j in range(1,3):
            rowList[i][j] = random.randint(1,9)

    print(rowList)

    loShuMG = lo_shu(rowList)
    

def lo_shu(magicSquare):
    k = 0
    sumVal = 0
    for k in range(1,3):
        sumVal += magicSquare[1][k]

    l = 0
    sumVal2 = 0
    for l in range(1, 3):
        sumVal2 += magicSquare[1][l]

    m = 0
    sumVal3 = 0
    for m in range(1, 3):
        sumVal3 += magicSquare[m][1]

    if sumVal == sumVal2 and sumVal == sumVal3:
        print('this is a lo shu magic square ', sumVal, sumVal2, sumVal3)
    else:
        print('this is not a lo shu magic square', sumVal, sumVal2, sumVal3)

main()
