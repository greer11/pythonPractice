

#Given a sequence of answers, return the same set of answers with all the 0's removed.
numList = [5, 3, 0, 2, 6, 2, 0, 7, 2, 5]

def cullZeros(numList):
    #newList = list(filter(lambda num: num != 0, numList))
    #return newList
    return [x for x in numList if x > 0]


def sortNumbersDesc(numList):
    sortedList = []
    sorting = True
    while sorting:
        n = len(numList)
        index = 0
        currentLargest = numList[0]
        for i in range(n-1):
            x = i+1
            if numList[x] > currentLargest:
                currentLargest = numList[x]
                index = x
        sortedList.append(currentLargest)
        numList.remove(numList[index])
        if not numList:
            sorting = False
    return sortedList

def lengthCheck(x, numList):
    if x > len(numList):
        return True
    else: return False

def frontElim(x, numList):
    for i in range(x):
        numList[i] -= 1
    return numList

# culledList = cullZeros(numList)
# print(f"new list is {culledList}")
#
# sortedList = sortNumbersDesc(culledList)
# print(f"the sorted numbers are {sortedList}")
#
# lengthCheckedList = lengthCheck(1, emptyList)
# print(f"the length check for the list returned: {lengthCheckedList}")
#
# frontElimList = frontElim(4, sortedList)
# print(f"the newest list is {frontElimList}")

#the havel-hakimi algorithm

def HavHak(numList):
    while True:
        print(f"starting anew with list: {numList}")
        culledList = cullZeros(numList)
        if (lengthCheck(1, culledList)):
            print("returning True")
            return True
        sortedList = sortNumbersDesc(culledList)
        print(f"the sorted list is {sortedList}")
        N = sortedList[0]
        sortedList.remove(sortedList[0])
        if (lengthCheck(N, sortedList)):
            print("returning false")
            return False
        numList = frontElim(N, sortedList)


testList = [16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]
HavHak(numList)
print("testing HavHak with a list that should return true")
HavHak(testList)