def handle_input(f):
    matrix = []
    for row in f.read().splitlines():
        column = [int(number) for number in row if row.isdigit()]
        matrix.append(column)
    return matrix

def solve_input(matrix):
    matrix_len = len(matrix)
    visible_trees = (matrix_len*4)-4
    for row in range(1, matrix_len-1):
        for col in range(1, matrix_len-1):
            if if_visible(matrix, row, col):
                visible_trees += 1
    return visible_trees

def if_visible(matrix, row, col):
    return check_left(matrix, row, col) or check_right(matrix, row, col) or check_buttom(matrix, row, col) or check_top(matrix, row, col)
    
def check_left(matrix, row, col):
    vis = True
    for i in range(0, col):
        if matrix[row][col] <= matrix[row][i]:
            vis = False
    return vis
    
def check_right(matrix, row, col):
    vis = True
    for i in range(col+1, len(matrix)):
        if matrix[row][col] <= matrix[row][i]:
            vis = False
    return vis
    
def check_top(matrix, row, col):
    vis = True
    for i in range(0, row):
        if matrix[row][col] <= matrix[i][col]:
            vis = False
    return vis
    
def check_buttom(matrix, row, col):
    vis = True
    for i in range(row+1, len(matrix)):
        if matrix[row][col] <= matrix[i][col]:
            vis = False
    return vis