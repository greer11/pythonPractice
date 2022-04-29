from urllib import request, error
from random import *

#get a random 5 letter word
url = request.urlopen("https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt")
content = url.read()
url.close()
strContent = content.decode().split('\n')
randomIndex = randint(0, len(strContent))
word = (strContent[randomIndex])

listWord = list(word)
count = 0
wrongLetters = []

userFacingWord = ['*', '*', '*', '*', '*']
print('Welcome to wordle!')
print(''.join(userFacingWord))

while count<6:

    userGuess = input("enter your guess: ")
    if len(userGuess) != 5:
        print("\nERROR: please enter a 5 letter word!")
        continue
    if userGuess not in strContent:
        print("\n please enter a real word!")
        continue

    indiciesToDelete = []
    for i in range(len(listWord)):
        if userGuess[i] in listWord:
            if userGuess[i] == listWord[i]:
                if userGuess[i] == userFacingWord[i]:
                    continue
                else:
                    userFacingWord[i] = ('\033[1;32;40m' + userGuess[i] + '\033[0m')
                    listWord[i] = 0

            else:
                userFacingWord[i] = ('\033[1;33;40m' + userGuess[i] + '\033[0m')
                indiciesToDelete.append(i)
        elif userGuess[i] in wrongLetters:
            continue
        else:
            wrongLetters.append(userGuess[i])
    #display info to user
    print(''.join(userFacingWord))

    #remake the user facing word without the letters in the wrong place
    for i in indiciesToDelete:
        userFacingWord[i] = '*'
    if userGuess == word:
        print('the word was:', word)
        print("\nYou've WON!!!")
        exit()
    else:
        print('')
        print('you have:', 6 - (count + 1), 'remaining attempts')
        print('wrong letters:', ''.join(wrongLetters))
    count += 1

print("\nsorry, you've lost")
print("the word was:", word)