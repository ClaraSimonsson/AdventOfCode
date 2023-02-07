
from Day_code import Day4 as day

def main():
    day_puzzle = 'Day4'
    day_input = '{}.txt'.format(day_puzzle)
    with open('puzzle_input/{}'.format(day_input)) as f:        
        input = day.handle_input(f)
    print(day.solve_input(input))


if __name__ == '__main__':
    main()