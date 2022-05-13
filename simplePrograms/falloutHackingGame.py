import random
import os
import numpy as np

def getWords(difficulty, maxWords):
    if os.path.isfile('enable1.txt'):
        f = open("enable1.txt", "r")
        s = (f.read()).split("\n")
        f.close()
        wordCount = 0
        wordList = []
        while wordCount < maxWords:
            index = random.randint(0, len(s))
            if len(s[index]) == 4+difficulty:
                if s[index] in wordList:
                    continue
                else:
                    wordList.append(s[index])
                    wordCount += 1
            continue
        return wordList
    else: print('file does not exist')

def decideWinner(wordList):
    index = random.randint(0, (len(wordList)-1))
    winningWord = wordList[index]
    return winningWord

def updateWords(wordList, guess):
    for w in range(len(wordList)):
        if wordList[w] == guess:
            length = len(wordList[w])
            wordList[w] = '*' * length
    return wordList

def displayWords(wordList):
    length = int((len(wordList))/2)
    newWordList = []
    for word in wordList:
        pos = str(hex(id(word)))
        newWord = pos + ": " + word
        newWordList.append(newWord)
    wordArray = np.reshape(newWordList, (length, 2))
    print("\n----remaining words----")
    print ("\033[1;32m")
    for w in range(len(wordArray)):
        print(wordArray[w])
    print("\033[1;0m")
    print("------------------------")

def playerGuess(winningWord):
    guess = input("please enter your guess: ")
    if guess == "stop":
        exit()
    elif guess.lower() == winningWord:
        print("\nYOU'VE WON!\n")
        return guess.lower(), True
    else:
        return guess.lower(), False

def selectDifficulty():
    difficulty = 0
    while difficulty < 1:
        diff = input("please select your difficulty: 1 - 10 ")
        if diff == "stop":
            exit()
        try:
            int(diff)
        except:
            print("please make sure your choice is a whole number between 1 and 10")
            continue
        if int(diff) < 1:
            print("please choose a number above 0")
            continue
        elif int(diff) > 10:
            print("please choose a number below 11")
            continue
        else:
            difficulty = int(diff)
    return difficulty

def determineSimilarity(guess, winningWord):
    lettersInCommon = 0
    for i in range(len(guess)):
        if guess[i] == winningWord[i]:
            lettersInCommon +=1
    return lettersInCommon



def main():
    while True:
        win = False
        diff = selectDifficulty()
        words = getWords(diff, 10)
        w = decideWinner(words)
        counter = 4
        while counter > 0:
            print(f"{counter} tries remaining")
            displayWords(words)
            guess = playerGuess(w)
            if guess[0] not in words:
                print(f"{guess[0]} isn't in the word list!")
                continue
            sim = determineSimilarity(guess[0], w)
            print(f"your guess has {sim} letters in common with the winning word")
            if guess[1]:
                break
            words = updateWords(words, guess[0])
            counter -= 1
            if counter == 0:
                print(f"\nsorry, you've lost, the word was {w}, please try again\n")

main()
