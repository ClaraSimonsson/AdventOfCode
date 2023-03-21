import re
import copy
def handle_input(f):
    levels, instructions = [section.split("\n") for section in f.read().split("\n\n")]
    levels = [crate.replace("    ", " [X] ") for crate in levels[:-1]]  # Replace empty space with [X], skip last line telling how many stacks it will be
    """for level in levels:
        print(level.split())
        for crate in level.split():
            print(crate[1])
    """
    levels = [[crate[1] for crate in level.split()] for level in levels]  # Get rid of brackets
    stacks = [[] for _ in range(len(levels[0]))]  # Create nested lists of number of vertical stacks
    for level in reversed(levels):
        for index, crate in enumerate(level):
            if crate != "X":
                stacks[index].append(crate)
    instructions = [re.findall("\d+", instruction) for instruction in instructions]
    return [stacks, instructions]   

def solve_input(input):
    stacks_separated = copy.deepcopy(input[0])
    stacks_together = copy.deepcopy(input[0])
    instructions = input[1]
    for instruction in instructions:
        crates_to_move = int(instruction[0])
        from_stack = int(instruction[1])-1
        to_stack = int(instruction[2])-1
        move_one_crate(stacks_separated, crates_to_move, from_stack, to_stack)
        move_several_crates(stacks_together, crates_to_move, from_stack, to_stack)
    return "".join([stack.pop() for stack in stacks_separated]), "".join([stack.pop() for stack in stacks_together if stack])

def move_one_crate(stacks, crates_to_move, from_stack, to_stack):
    i = 0
    while i < crates_to_move:
        crate = stacks[from_stack].pop()
        stacks[to_stack].append(crate) 
        i += 1

def move_several_crates(stacks, crates_to_move, from_stack, to_stack):
    i = 0
    crates = []
    while i < crates_to_move:
        crate = stacks[from_stack].pop()
        crates.append(crate)
        i += 1
    [stacks[to_stack].append(crate) for crate in crates[::-1]]
    