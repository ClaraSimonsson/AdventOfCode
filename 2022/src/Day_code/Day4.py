import re

def handle_input(f):
    pairs = []
    for line in f.readlines():
        pair = re.split('[-,]', line.strip())
        first = set(range(int(pair[0]), int(pair[1])+1))
        sec = set(range(int(pair[2]), int(pair[3])+1))
        pairs.append([first, sec])
    return pairs

def solve_input(input):
    overlap = 0
    contains = 0
    for pair in input:
        first_set = pair[0]
        sec_set = pair[1]
        shortest = min(len(first_set), len(sec_set))
        intersect = first_set.intersection(sec_set)
        if len(intersect) == shortest:
            contains += 1
        if intersect:
            overlap += 1
    return contains, overlap