from collections import defaultdict

def handle_input(f):
    return f.readlines()

def solve_input(input):
    dir_sizes = sumSizes(input)
    sum = 0
    for k in dir_sizes:
        current_size = dir_sizes.get(k)
        sum += current_size if current_size <= 100000 else 0
    return sum

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
