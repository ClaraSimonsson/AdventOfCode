def handle_input(f):
    matrix = []
    for row in f.read().splitlines():
        column = [int(number) for number in row if row.isdigit()]
        matrix.append(column)
    return matrix

def solve_input(matrix):
    matrix_len = len(matrix)
    visible_trees = (matrix_len*4)-4
    highest_scenic_score = 0
    for row in range(1, matrix_len-1):
        for col in range(1, matrix_len-1):
            visible, scenic_score = if_visible(matrix, row, col)
            visible_trees += 1 if visible else 0
            highest_scenic_score = scenic_score if (scenic_score > highest_scenic_score) else highest_scenic_score
    return [visible_trees, highest_scenic_score]

def if_visible(matrix, row, col):
    visible = False
    left_vis, left_score = check_left(matrix, row, col)
    right_vis, right_score = check_right(matrix, row, col)
    buttom_vis, buttom_score = check_buttom(matrix, row, col)
    top_vis, top_score = check_top(matrix, row, col)
    if (left_vis or right_vis or buttom_vis or top_vis):
        visible = True
    score = left_score * right_score * buttom_score * top_score
    return [visible, score]
    
def check_left(matrix, row, col):
    vis = True
    score = 0
    for i in reversed(range(0, col)):
        if matrix[row][col] <= matrix[row][i]:
            vis = False
            score += 1
            break
        score += 1
    return [vis, score]
    
def check_right(matrix, row, col):
    vis = True
    score = 0
    for i in range(col+1, len(matrix)):
        if matrix[row][col] <= matrix[row][i]:
            vis = False
            score += 1
            break
        score += 1
    return [vis, score]
    
def check_top(matrix, row, col):
    vis = True
    score = 0
    for i in reversed(range(0, row)):
        if matrix[row][col] <= matrix[i][col]:
            vis = False
            score += 1
            break
        score += 1
    return [vis, score]
    
def check_buttom(matrix, row, col):
    vis = True
    score = 0
    for i in range(row+1, len(matrix)):
        if matrix[row][col] <= matrix[i][col]:
            vis = False
            score += 1
            break
        score += 1
    return [vis, score]