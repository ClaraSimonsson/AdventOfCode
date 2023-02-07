from textwrap import wrap
from collections import Counter
# Find shared types (identical chars)
# Find its priority
    # lowercase has priority 1-26
    # uppercase has priority 27-52
# Summerize the priorities

# 1. map input to a final list: the list should include a list with two items, 
# one for each compartment of the rucksack
def create_compartments(items):
    half_size = int(len(items)/2)
    return wrap(items, half_size)

def find_groups(rucksacks):
    groups = []
    for idx in range(0, len(rucksacks), 3):
        groups.append(rucksacks[idx:idx+3])
    return groups

def calc_sum(rucksacks):
    priority_sum = 0
    for rucksack in rucksacks:
        com_char = find_the_com_item(rucksack)
        priority_sum += find_priority(com_char)
    return priority_sum

def find_the_com_item(rucksacks):
    com_item_list = []
    first_rucksack = rucksacks[0]
    list_len = len(rucksacks)
    for char in first_rucksack:
        if (char in rucksacks[1]) and (char in rucksacks[2]):
            com_item_list.append(char)
    return com_item_list
    
def find_the_item(com_item_list):
    string = ""
    string = string.join(com_item_list)
    counter = Counter(string)

    most_frequent = counter.most_common(1)[0]
    return [most_frequent[0]]
    

def calc_priority_sum(rucksacks):
    priority_sum = 0
    for rucksack in rucksacks:
        com_char = find_com_item(rucksack)
        priority_sum += find_priority(com_char)
    return priority_sum
        
        
# 2. Go through both strings and try to find common types
def find_com_item(rucksacks):
    com_item_list = []
    first_rucksack = rucksacks[0]
    for char in first_rucksack:
        for rucksack in rucksacks[1:]:
            if char in rucksack:
                com_item_list.append(char)
    return com_item_list
        
        
def find_priority(com_char):
    types = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return (types.index(com_char[0]) + 1)
    
    
def handle_input(f):
    rucksacks = []
    [rucksacks.append(line.strip()) for line in f.readlines()]
    return rucksacks


def solve_input(rucksacks):
    new_rucksacks = (map(create_compartments, rucksacks))
    group_rucksacks = find_groups(rucksacks)
    return calc_priority_sum(new_rucksacks), calc_sum(group_rucksacks)
    
""" def main():
    rucksacks = []
    with open('rucksack.txt') as f:
        [rucksacks.append(line.strip()) for line in f.readlines()]
    new_rucksacks = (map(create_compartments, rucksacks))
    tot = calc_priority_sum(new_rucksacks)
    print(tot)
    
    group_rucksacks = find_groups(rucksacks)
    tot_prior = calc_sum(group_rucksacks)
    print(tot_prior)
    

if __name__ == '__main__':
    main() """