import re 


def func():
    sum = 0
    with open("input.txt", "r") as f:
        for line in f:
            if possibility(line):
                sum += int(line[5:7])
    print(sum)

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

if __name__ == "__main__":
    func()