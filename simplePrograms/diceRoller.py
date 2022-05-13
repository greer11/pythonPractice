import random
import re


def roll(numOfDice, diceSides):
    dice = []
    num = 0
    for i in range(numOfDice):
        rolled = random.randrange(1, diceSides+1)
        dice.append(rolled)
        num += rolled
    return num, dice


def run():
    rolling = True
    while rolling:
        command = input("enter a roll ")
        if command == "stop":
            rolling = False
            continue
        try:
            slist = command.split("d")
            numOfDice = int(slist[0])
            diceSides = int(slist[1])
        except:
            print("please make sure you enter a valid command in _d_ format, where _ is a valid integer\nIf you're finished please enter 'stop'")
            continue
        try:
            roller = roll(numOfDice, diceSides)
        except:
            print("invalid dice selection, please try again")
            continue
        print(f"{roller[0]} : {roller[1]}")
