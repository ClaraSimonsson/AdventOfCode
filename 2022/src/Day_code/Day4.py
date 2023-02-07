import re

def handle_input(f):
    for line in f.readlines():
        pairs = re.split('[, -]', line.strip())
        print(pairs)

def solve_input(input):
    pass