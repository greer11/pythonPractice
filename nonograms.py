'''
Given a binary array of any length,
return an array of positive integers that represent
the lengths of the sets of consecutive 1's in the input array,
in order from left to right.
'''

def nonogram(arr):
    result = []
    resIndex = 0
    curVal = 0
    for i in range(len(arr)):
        #flag a found 1
        if arr[i] == 1:
            #append a new number so that we don't get an index error
            if curVal == 0:
                result.append(1)
            else:
                result[resIndex] += 1
        #change index when finding a zero after a 1
        if arr[i] == 0:
            if curVal == 1:
                resIndex += 1
        #if arr[i] == 0:
        curVal = arr[i]
    print(result)


arr = [0,0,0,1,1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1]
nonogram(arr)