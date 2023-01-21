'''
Write a function, which takes a non-negative integer (seconds)
as input and returns the time in a human-readable countdown style, formatted as such: "##d ##h ##m ##s"

- The time numbers should be padded to two digits (Eg. 00-99)
- The timer format should only contain days, hours, minutes, and seconds

For example: Given 323343, the output should be 03d 17h 49m 03s
Given this integer 788617, output the formatted string.
'''

def GetDays(seconds):
    minutes = seconds/60
    hours = minutes/60
    days = hours/24
    intDays = int(days)
    hoursToSubtract = intDays* 24
    minutesToSubtract = hoursToSubtract * 60
    secondsToSubtract = minutesToSubtract * 60
    return intDays, secondsToSubtract

def GetHours(seconds):
    minutes = seconds/60
    hours = minutes/60
    #get the amount of hours to the nearest whole number
    intHours = int(hours)
    minutesToSubtract = intHours * 60
    secondsToSubtract = minutesToSubtract * 60
    return intHours, secondsToSubtract

def GetMinutes(seconds):
    minutes = seconds/60
    intMinutes = int(minutes)
    secondsToSubtract = intMinutes * 60
    return intMinutes, secondsToSubtract

def CalculateTime(seconds):
    remainingSeconds = seconds
    days = GetDays(seconds)
    remainingSeconds -= days[1]
    hours = GetHours(remainingSeconds)
    remainingSeconds -= hours[1]
    minutes = GetMinutes(remainingSeconds)
    remainingSeconds -= minutes[1]
    seconds = remainingSeconds
    string = f"{days[0]:02d}d {hours[0]:02d}h {minutes[0]:02d}m {remainingSeconds:02d}s"
    print(string)
    return string


CalculateTime(788617)

#the rerult is:
# 09d 03h 03m 37s
