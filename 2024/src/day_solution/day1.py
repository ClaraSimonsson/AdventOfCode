def handle_input(f):
    list1, list2 = [], []
    for row in f.read().splitlines():
        list1.append(row.split('   ')[0])
        list2.append(row.split('   ')[1])
    return [list1, list2]

def solve_input(input):
    list1 = sorted(input[0])
    list2 = sorted(input[1])
    tot_diff = 0
    # Part 1
    # for i in range(len(list1)):
    #     tot_diff += abs(int(list1[i]) - int(list2[i]))
        
    # Part 2
    sim_score = 0
    for nr in list1:
        appearances = list2.count(nr)
        sim_score += int(nr) * appearances
    return sim_score