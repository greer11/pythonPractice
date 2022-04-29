'''
set of coin denominations:
500, 100, 25, 10, 1
given a number, make change with as many of the largest coins you can
for example 672 = 1 * 500, 1 * 400, 2 * 25, 2 * 10, and 2 * 1
count the total number of coins
'''

def countCoins(number):
    totalCoins = 0
    coinList = [500, 100, 25, 10, 1]
    for i in range(len(coinList)):
        while number >= coinList[i]:
            number -= coinList[i]
            totalCoins +=1
            print("give one ", coinList[i])
    return totalCoins

print(countCoins(672))