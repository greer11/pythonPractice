"""First, you mash in a random large number to start with. Then, repeatedly do the following:

If the number is divisible by 3, divide it by 3.
If it's not, either add 1 or subtract 1 (to make it divisible by 3), then divide it by 3.
The game stops when you reach "1"."""
import random

#mash large number, for practice use 100

num = 100

def canDivideBy3(num):
    if num%3 == 0:
        return True
    else: return False

def gameOfThree(num):
    while num != 1:
        initial_num = num
        rounds = 0
        factor = "+/- 0"
        if canDivideBy3(num):
            num = num/3
        else:
            if canDivideBy3(num+1):
                num = (num+1)/3
                factor = "+ 1"
            elif canDivideBy3(num-1):
                num = (num-1)/3
                factor = "- 1"
        print(f"{initial_num} {factor}")
    print(num)

gameOfThree(31337357)