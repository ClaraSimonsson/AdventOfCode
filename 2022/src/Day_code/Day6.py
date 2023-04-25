def handle_input(f):
    return f.read().split("\n")

def solve_input(input):
    seq = input[0]
    dist_chars_p1 = 4
    dist_chars_p2 = 14
    return [get_dist_char_pos(seq, dist_chars_p1), get_dist_char_pos(seq, dist_chars_p2)]

def get_dist_char_pos(seq, dist_chars):
    for i in range(len(seq)):
        last_char_pos = i+dist_chars
        char_set = get_char_set(seq, i, last_char_pos)
        if (len(char_set) == dist_chars):
            return last_char_pos
    return -1

def get_char_set(seq, i , last_char_pos):
    char_set = set()
    [(char_set.add(char)) for char in seq[i:last_char_pos]]
    return char_set