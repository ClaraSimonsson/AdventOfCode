
def input_to_dict(content):
    p1 = content[0]
    p2 = content[-1]
    return [p1,p2]
    
def handle_input(f):
    content = []
    [content.append(line.strip()) for line in f.readlines()]
    return content

def game(strat_list):
    total_points = 0
    # for every value in both list, compare to each other
    for round in strat_list:
        # total_points += play_round(round)
        total_points += play_another_strat(round)
    return total_points
            

def play_round(round_strat):
    p1 = create_int(round_strat[0])
    p2 = create_int(round_strat[1])
    round_point = p2 + outcome_points(p1, p2)
    return round_point


def create_int(player_choice): 
    match player_choice:
        # Rock
        case 'A' | 'X':
            return 1
        # Paper
        case 'B' | 'Y':
            return 2
        # Scissor
        case 'C' | 'Z':
            return 3


def outcome_points(p1, p2):
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
    # 1 defeats 3, 3 defeats 2, 2 defeats 1
    if (p1 == p2):
        return 3
    if p1 > p2 or (p1 == 1 and p2 == 3):
        if (p1 == 3 and p2 == 1):
            return 6
        else:
            return 0
    else:
        return 6
           
def play_another_strat(round_strat):
    p1 = create_int(round_strat[0])
    outcome = create_outcome(round_strat[1])
    round_point = outcome + make_choice(p1, outcome)
    return round_point

def create_outcome(outcome):
    match outcome:
        case 'A' | 'X':
            return 0
        # Paper
        case 'B' | 'Y':
            return 3
        # Scissor
        case 'C' | 'Z':
            return 6
        
def make_choice(p1, outcome):
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
    # 1 defeats 3, 3 defeats 2, 2 defeats 1
    match outcome:
        case 0:
            if p1 == 1: return 3
            if p1 == 2: return 1
            if p1 == 3: return 2
        case 3:
            if p1 == 1: return 1
            if p1 == 2: return 2                
            if p1 == 3: return 3
        case 6:
            if p1 == 1: return 2
            if p1 == 2: return 3
            if p1 == 3: return 1  
            

def solve_input(input):
    round_list = map(input_to_dict, input)
    return game(list(round_list))
""" 
def main():
    content = []
    with open('strategy_guide.txt') as f:
        [content.append(line.strip()) for line in f.readlines()]
    round_list = map(input_to_dict, content)
    total_points = game(list(round_list))
    print(total_points)

if __name__ == '__main__':
    main() """