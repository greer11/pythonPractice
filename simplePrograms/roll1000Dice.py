from diceRoller import roll
d = {"1": 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0}

x = 0
while x < 1000:
    print(x)
    new_roll = roll(5, 6)
    list = new_roll[1]
    for i in range(len(list)):
        d[str(list[i])] += 1
    x+=1
print(d)