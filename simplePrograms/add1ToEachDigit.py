'''
A number is input in computer then a new no should get printed by adding one to each of its digit.
If you encounter a 9, insert a 10 (don't carry over, just shift things around).
For example, 998 becomes 10109.
'''
import math

def getDigitLenWithMath(number):
    if number < 999999999999998:
        return int(math.log10(number))+1
    else: return int(math.log10(number))

def getDigitLenWithString(number):
    strNum = str(number)
    return len(strNum)

def createNumToAdd(length):
    result = 0
    for i in range(length):
        result += 10**i
    return result

def addNumbers(original_num, ones):
    strOrNum = [i for i in str(original_num)]
    strOnes = [i for i in str(ones)]
    digits = len(strOrNum)
    for i in range(digits):
        print(strOrNum[i])
        print(strOnes[i])
        newnum = int(strOrNum[i]) + int(strOnes[i])
        strOrNum[i] = str(newnum)
        print(strOrNum[i])
    return int(''.join(strOrNum))




number = 998

length = (getDigitLenWithMath(number))
numToAdd = createNumToAdd(length)
addedNums = addNumbers(number, numToAdd)
#finalResult = number+numToAdd
print(number)
print(numToAdd)
#print(finalResult)
print(addedNums)