from collections import defaultdict

def handle_input(f):
    return f.readlines()

def solve_input(input):
    dir_sizes = sumSizes(input)
    tot_size = dir_sizes.get('/')
    unused_space = 70000000 - tot_size
    sum = 0     # total size of all directories with a size of at most 100 000
    smallest_dir_size = tot_size        # Size of smallest directory to delete to reach 30 000 000 of unused space
    for k in dir_sizes:
        current_size = dir_sizes.get(k)
        sum += add_size_below_limit(current_size)
        if (if_enough_unused_space(unused_space + current_size)) and (current_size < smallest_dir_size):
            smallest_dir_size = current_size
    return [sum, smallest_dir_size]

def add_size_below_limit(current_size):
    return current_size if current_size <= 100000 else 0

def if_enough_unused_space(tot_space):
    return (tot_space) >= 30000000
    

def sumSizes(input):
    stack = []
    file_sizes = defaultdict(int)
    for cmd in input: 
        if cmd.startswith("$ ls") or cmd.startswith("dir"):
            continue
        if cmd.startswith("$ cd"):
            dir = cmd.split()[2]
            if dir == "..":
                stack.pop()
            else:
                path = f"{stack[-1]}_{dir}" if stack else dir
                stack.append(path)
        else:
            size, file = cmd.split()
            for path in stack:
                file_sizes[path] += int(size)
    return file_sizes
