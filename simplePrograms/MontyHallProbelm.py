#3 doors, random one contains prize
#contestant selects a door
#monty selects one of the other doors that **doesn't** contain a prize
#contestant can choose to switch
import random

def run(switch, contestant_door):
    did_win = 0
    doors = [1, 2, 3]
    remaining_doors = [1, 2, 3]
    available_doors = [1, 2, 3]

    #select a random door
    prize_door_index = int(random.randrange(0, len(doors)))
    winning_door = doors[prize_door_index]
    remaining_doors.remove(winning_door)

    #contestant can selects a door
    # if not chosen_door:
    #     #     print("chosen door is none")
    #     #     contestant_door_index = int(random.randrange(0, len(doors)))
    #     #     contestant_door = doors[contestant_door_index]
    #     #     print('random contestant door: ', contestant_door)
    #     # else:
    #     #     print(chosen_door.values()[0])
    #     #     print("chosen door is: ",)
    #     #     contestant_door = chosen_door
    if contestant_door != winning_door:
        remaining_doors.remove(contestant_door)



    #monty hall opens 1 door that doesnt contain prize
    if len(remaining_doors) == 1:
        monty_hall_door = remaining_doors[0]
    else:
        monty_hall_door_index = int(random.randrange(0, len(remaining_doors)))
        monty_hall_door = remaining_doors[monty_hall_door_index]
    available_doors.remove(monty_hall_door)

    #print('contestant door is: ', contestant_door)
    #print('Monty chooses: ', monty_hall_door)
    #print("switch? ", switch)

    if switch == True:
        if contestant_door != available_doors[0]:
            contestant_door = available_doors[0]
        else: contestant_door = available_doors[1]
        #print("contestant's new door is: ", contestant_door)
    #print('Winning door is: ', winning_door)
    if winning_door == contestant_door:
        did_win = 1
        #print("Contestant won!")
    return did_win

def calculateWinRate(switch, contestant_door, iterations):
    wins = 0
    i = 0
    while i < iterations:
        value = run(switch, contestant_door)
        wins += value
        i += 1
    win_percentage = wins/iterations
    return wins, win_percentage


'''Alice always choose door number one, and stays with door number 1
bob always chooses number 1 and switches'''


print("ALICE")
print("Alice chooses door #1 and doesn't switch")
alice = calculateWinRate(False, 1, 1000)

print("out of 1000 games Alice wins a total of: ", alice[0])
print("that means Alice wins:", alice[1], "% of the time\n\n")

print("BOB")
print("Bob chooses door #1 but always switches")
bob = calculateWinRate(True, 1, 1000)

print("out of 1000 games Bob wins a total of: ", bob[0])
print("that means Bob wins:", bob[1], "% of the time")






