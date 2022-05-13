numList = [5, 3, 0, 2, 6, 2, 0, 7, 2, 5]

def sortNumbersDesc(numList):
    sortedList = []
    sorting = True
    while sorting:
        n = len(numList)
        index = 0
        currentLargest = numList[0]
        for i in range(n-1):
            #print(f"current i is {i}")
            x = i+1
            print(f"current x is {numList[x]}")
            if numList[x] > currentLargest:
                print(f"{numList[x]} is larger than {currentLargest}")
                currentLargest = numList[x]
                index = x
        sortedList.append(currentLargest)
        numList.remove(numList[index])
        if not numList:
            sorting = False
    return sortedList

newList = sortNumbersDesc(numList)
print(f"new list is: {newList}")