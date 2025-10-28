import re

def handle_input(f):
    mul_instructions = []
    do_strings = re.split("do\(\)", f.read())
    for str in do_strings:
        if (re.search("don't\(\)", str)):
            do_dont_range = re.search("don't\(\)", str)
            mul_instr = str[:do_dont_range.start()]
            mul_instructions.extend(re.findall("mul\((\d{1,3}),(\d{1,3})\)", mul_instr))
        else:
            mul_instructions.extend(re.findall("mul\((\d{1,3}),(\d{1,3})\)", str))
    return mul_instructions

def solve_input(input):
    tot = 0
    for mul in input:
        val1 = int(mul[0])
        val2 = int(mul[1])
        tot += (val1*val2)
    return tot