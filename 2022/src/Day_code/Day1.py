# Day 1
import sys
# Create list from text file, separate by new line
# if next is empty line, add the list to another list

def create_lists(input_list):
    # input_list = create_input_list()
    total_cal_list = count_total_cals(input_list)
    #print(max(total_cal_list))
    top_three = find_top_three(total_cal_list)
    #print(top_three)
    return max(total_cal_list), top_three
    
def create_input_list():
    cals_elves = []
    with open('../puzzle_input/Day1') as f:
        cals_elf = []
        for line in f.readlines():
            line = line.strip()
            if (line != ""):
                cals_elf.append(line)
            else:
                cals_elves.append(cals_elf)
                cals_elf = []
    return cals_elves

def handle_input(f):
    cals_elves = []
    cals_elf = []
    for line in f.readlines():
        line = line.strip()
        if (line != ""):
            cals_elf.append(line)
        else:
            cals_elves.append(cals_elf)
            cals_elf = []
    return cals_elves
    
    

def count_total_cals(input_list):
    tot_cals = []
    for list in input_list:
        tot_cals.append(calculate_elf_cals(list))
    return tot_cals
    
    
def calculate_elf_cals(cal_list):
    tot = 0
    for nr in cal_list:
        nr = int(nr)
        tot += nr
    return tot


def find_top_three(all_elves):
    first = all_elves[0]
    second = all_elves[1]
    third = all_elves[2]
    for elf in all_elves[2:]:
        if elf > third:
            tmp_2 = second
            if elf > second:
                tmp_1 = first
                if elf > first:
                    first = elf
                    second = tmp_1
                    third = tmp_2
                else:
                    second = elf
                    third = tmp_2
            else:
                third = elf
    return first + second + third

def solve_input(input):
    return create_lists(input)
                      
"""     
def main():
    create_lists()

if __name__ == '__main__':
    main() """