#!/usr/bin/python3

# code where the data.tx file is read on each line, the calibration 
# value can be found by combining the first digit and the last digit
# (in that order) to form a single two-digit number, and if there is only one digit on that line, it combines
# the digit with itself to form a two-digit number. the programm then adds up all these numbers and prints the result.

def getnumber(line):
    nums = []
    for a in line:
        if a.isdigit():
            nums.append(int(a))
    if len(nums) == 1:
        number = str(nums[0]) + str(nums[0])
    else:
        number = str(nums[0]) + str(nums[-1])
    return int(number)

# open the file
def main():
    # open the file
    with open('data.txt', 'r') as data:
        arr = []
        for line in data:
            arr.append(getnumber(line))
    print(sum(arr))
        
# call the main function
if __name__ == '__main__':
    main()

