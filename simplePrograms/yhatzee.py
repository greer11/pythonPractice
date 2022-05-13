import time
from diceRoller import roll

def countNumbers(numList):
    numbersDict = {}
    for k in numList:
        numbersDict[str(k)] = 0
    for i in range(len(numList)):
        numbersDict[str(numList[i])] += 1
    return numbersDict

def yhatzee_upper(numDict):
    for k in numDict:
        numDict[k] = int(k) * numDict[k]
    totals_list = []
    for i in numDict:
        totals_list.append(numDict[i])
    return max(totals_list)


timeA = time.time()
roll_dice = roll(100000, 999999999)
list = roll_dice[1]
numDict = countNumbers(list)
yhatzee = yhatzee_upper(numDict)
print(yhatzee)
timeB = time.time()
totaltime = timeB - timeA
print(f"total compute time was {totaltime}")
