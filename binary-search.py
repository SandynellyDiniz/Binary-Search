import math

list = [2, 10, 15, 17, 21, 28, 40, 55, 60, 61, 62]

def searchBinary(value, search):
    posLi = 0
    posLs = len(value) - 1
    while posLi <= posLs:
        posMore = (posLi + posLs) // 2
        shot = value[posMore]

        if shot == search:
            return posMore
        if shot > search:
            posLs = posMore - 1
        else:
            posLi = posMore + 1
    return -1

print(searchBinary(list, 28))