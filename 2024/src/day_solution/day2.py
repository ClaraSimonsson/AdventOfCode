def handle_input(f):
    return [row.split(' ') for row in f.read().splitlines()]

def solve_input(input):
    safe = 0
    safe_reports = []
    for report in input:
        diff = calc_diff(report, 1, 0)
        if not out_of_bounds(diff):
            is_dec = is_decreasing(diff)
            for i in range(1, len(report)):
                diff = calc_diff(report, i, i-1)
                if (out_of_bounds(diff) or (diff < 0 and is_dec == False) or (diff > 0 and is_dec == True)):
                    break
                if (i == len(report) - 1):
                    safe += 1
                    safe_reports.append(report)
    
    unsafe_reports = []
    for report in input:
        if report not in safe_reports:
            unsafe_reports.append(report)
  
    for report in unsafe_reports:
        safe += check_each_combination(report)
    return safe

def calc_diff(report, i, i_previous):
    return int(report[i_previous]) - int(report[i])

def out_of_bounds(diff):
    if not (1 <= abs(diff) <= 3):
        return True
    return False

def is_decreasing(diff):
    if diff < 0:
        return True
    return False

def check_each_combination(report):
    safe = 0
    for i in range(0, len(report)):
        if i == 0:
            new_list = report[i+1:len(report)]
        elif i == len(report) - 1:
            new_list = report[0:i]
        else:
            before_i = report[0:i]
            after_i = report[i+1:len(report)]
            new_list = before_i + after_i
        diff = calc_diff(new_list, 1, 0)
        if not out_of_bounds(diff):
            is_dec = is_decreasing(diff)
            for i in range(1, len(new_list)):
                diff = calc_diff(new_list, i, i-1)
                if (out_of_bounds(diff) or (diff < 0 and is_dec == False) or (diff > 0 and is_dec == True)):
                    break
                if (i == len(new_list) - 1):
                    safe += 1
        if safe == 1:
            break
    return safe