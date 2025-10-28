from collections import defaultdict
from typing import Dict, Tuple


def handle_input(f):
    ls = f.read().splitlines()
    d = defaultdict(str)
    for i, row in enumerate(ls):
        for j, col in enumerate(row):
            d[(i, j)] = col
    return d


def solve_input(input: Dict[Tuple[int, int], str]) -> int:
    xmas_count = 0
    d = input
    allowed = ["MAS", "SAM"]
    # Part 1
    """  
   for i, j in list(d.keys()):
        for di in diagonals:
            for dj in diagonals:
                word = ''
                for n in range(4):
                    word = word + d[i+di*n, j+dj*n]
                xmas_count += (1 if 'XMAS' in word else 0) """
    # Part 2
    d_keys = list(d.keys())

    if not d_keys:
        return 0

    last_i = d_keys[-1][0]
    last_j = d_keys[-1][1]
    
    for i, j in d_keys:
        if i == 0 or j == 0 or i == last_i or j == last_j:
            continue
        top_left = d[(i - 1, j - 1)]
        top_right = d[(i - 1, j + 1)]
        bottom_left = d[(i + 1, j - 1)]
        bottom_right = d[(i + 1, j + 1)]
        current_char = d[(i, j)]
        d1 = top_left + current_char + bottom_right
        d2 = top_right + current_char + bottom_left
        if d1 in allowed and d2 in allowed:
            xmas_count += 1
    return xmas_count
