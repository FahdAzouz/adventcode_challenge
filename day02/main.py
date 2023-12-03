import re 


def func():
    sum = 0
    with open("input", "r") as data:
        for line in data:
            if possibility(line):
                sum =+ int(line[5:7])
    print(sum)

def possibility(line):
    arr = re.split(", |;", line)