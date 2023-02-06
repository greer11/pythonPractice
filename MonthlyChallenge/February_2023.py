'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''

def getCommonDivisible(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def run(maxNumber):
    multiple = 1
    for i in range(1, maxNumber + 1):
        multiple = multiple * i // getCommonDivisible(multiple, i)
    return multiple

result = run(20)
print(result)

