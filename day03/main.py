import re

def parse_input(input_string):
    # Parse the input string and return a 2D list representing the engine schematic
    return [list(line) for line in input_string.strip().split('\n')]

def is_symbol(char):
    # Check if a character is a symbol
    return char in ['*', '+', '$', '#', ...]  # Add any other symbols if needed

def get_adjacent_numbers(engine, row, col):
    # Get all adjacent numbers to a given position (including diagonals)
    rows, cols = len(engine), len(engine[0])
    numbers = []

    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if 0 <= i < rows and 0 <= j < cols and (i != row or j != col):
                if engine[i][j].isdigit():  # Check if the character is a digit
                    numbers.append(int(engine[i][j]))

    return numbers

def find_part_numbers(engine):
    part_numbers = set()

    for i in range(len(engine)):
        for j in range(len(engine[0])):
            if engine[i][j].isdigit() and any(is_symbol(engine[x][y]) for x, y in get_adjacent_numbers(engine, i, j)):
                part_numbers.add(int(engine[i][j]))

    return part_numbers

def sum_of_part_numbers(input_string):
    engine = parse_input(input_string)
    part_numbers = find_part_numbers(engine)
    return sum(part_numbers)

# Read input from file
with open('/home/fahd/adventcode_challenge/day03/input.txt', 'r') as f:
    input_string = f.read()

result = sum_of_part_numbers(input_string)
print(result)