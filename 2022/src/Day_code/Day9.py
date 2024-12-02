def handle_input(f):
    return [row.split(' ') for row in f.read().splitlines()]

def solve_input(input):
    coordinates = create_rope(9)
    visited_positions = set()
    visited_positions.add(coordinates.get(9))
    for instruction in input:
        direction = instruction[0]
        steps = int(instruction[1])
        coordinates, visited_positions = move_rope(direction, steps, coordinates, visited_positions)
    print_coords(visited_positions)
    return len(visited_positions)

def print_coords(visited_positions):
    min_x, max_x, min_y, max_y = find_interval(visited_positions)
    for row in range(min_y, max_y+1):
        str = ''
        for col in range(min_x, max_x+1):
            if ((col, row) in visited_positions):
                str = str + '#'
            else:
                str = str + '.'
        print(str)
    
def find_interval(visited_positions):
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    for x, y in visited_positions:
        if (x < min_x):
            min_x = x
        elif (x > max_x):
            max_x = x
        if (y < min_y):
            min_y = y
        elif (y > max_y):
            max_y = y
    return min_x, max_x, min_y, max_y

def create_rope(nr_knots):
    rope = dict(H=(0,0))
    for i in range(1, nr_knots+1):
        rope[i] = (0,0)
    return rope

def move_rope(direction, steps, coordinates, visited_positions):
    head = coordinates.get('H')
    #tail = coordinates.get('T')
    for _ in range(0, steps): 
        for key, val in coordinates.items():
            if (key == 'H'):
                head = move_head(direction, head) 
                previous_coords = head
            else:
                coordinates[key] = move_tail(previous_coords, val)
                previous_coords = coordinates[key]
        #tail = move_tail(head, tail)
        visited_positions.add(coordinates[9])
    coordinates[head] = head
    return coordinates, visited_positions
        
def move_head(direction, coord):
    x, y = get_coordinates(coord)
    match direction:
        case 'R':
            return (x+1, y)
        case 'D':
            return (x, y+1)
        case 'L':
            return (x-1, y)
        case 'U':
            return (x, y-1)
        
def move_tail(head, tail):
    t_x, t_y = get_coordinates(tail)
    h_x, h_y = get_coordinates(head)
    x_diff = h_x - t_x
    y_diff = h_y - t_y
    if((abs(x_diff) >= 2) or (abs(y_diff) >= 2)):
        if (change_in_y_dir(head, tail)):
            t_y = update_direction_coord(t_y, h_y, y_diff)
        elif (change_in_x_dir(head, tail)):
            t_x = update_direction_coord(t_x, h_x, x_diff)
        else:
            t_x = update_diagonal_coords(t_x, x_diff)
            t_y = update_diagonal_coords(t_y, y_diff)
    return (t_x, t_y)

def update_direction_coord(old_coord, head_coord, direction_diff):
    return old_coord + 1 if (abs(head_coord - (old_coord + 1)) < direction_diff) else old_coord - 1

def update_diagonal_coords(old_coord, direction_diff):
    return old_coord - 1 if direction_diff < 0 else old_coord + 1   

def change_in_x_dir(head, tail):
    t_x, t_y = get_coordinates(tail)
    h_x, h_y = get_coordinates(head)
    return t_x != h_x and t_y == h_y

def change_in_y_dir(head, tail):
    t_x, t_y = get_coordinates(tail)
    h_x, h_y = get_coordinates(head)
    return t_x == h_x and t_y != h_y

def get_coordinates(obj):
    return obj[0], obj[1]
    
    