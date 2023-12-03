import re 
import os

def func():
    power = 0
    highred = 0
    highgreen = 0
    highblue = 0
    file_path = "/home/fahd/adventcode_challenge/day02/input.txt"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                highred, highgreen, highblue = function(line, highred, highgreen, highblue)
                power = power + highred * highgreen * highblue
        print(power)

'''
Part 1
def possibility(line):
    arr = re.split(", |;", line)
    for string in arr:
        if "red" in string:
            for s in string.split():
                if s.isdigit() and int(s) > 12:
                    return False
        if "green" in string:
            for s in string.split():
                if s.isdigit() and int(s) > 13:
                    return False
        if "blue" in string:
            for s in string.split():
                if s.isdigit() and int(s) > 14:
                    return False
    return True
'''

# Part 2
def function(line, highred, highgreen, highblue):
    arr = re.split(", |;", line)
    for string in arr:
        if "red" in string:
            for s in string.split():
                if s.isdigit() and int(s) > highred:
                    highred = int(s)
        if "green" in string:
            for s in string.split():
                if s.isdigit() and int(s) > highgreen:
                    highgreen = int(s)

        if "blue" in string:
            for s in string.split():
                if s.isdigit() and int(s) > highblue:
                    highblue = int(s)
    return highred, highgreen, highblue

if __name__ == "__main__":
    func()