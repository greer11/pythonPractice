from urllib import request, error
from random import *

url = request.urlopen("https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt")
content = url.read()
url.close()
strContent = content.decode().split('\n')
randomIndex = randint(0, len(strContent))
word =(strContent[randomIndex])