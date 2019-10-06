# back-tracking (Constraint Satisfaction Problem, CSP) 

def is_repeat(puzzle, row, col, num):
    for i in range(9):
        if puzzle[row][i] == num:
            return True
    
    for i in range(9):
        if puzzle[i][col] == num:
            return True

    block_x = int(row / 3) * 3
    block_y = int(col / 3) * 3
    for i in range(block_x, block_x + 3):
        for j in range(block_y, block_y + 3):
            if puzzle[i][j] == num:
                return True
    return False

def solve_puzzle(puzzle, row, col):
    if row > 8:
        return True 

    if puzzle[row][col] == 0:
        for i in range(1, 10):
            if not is_repeat(puzzle, row, col, i):
                puzzle[row][col] = i
                if solve_puzzle(puzzle, int(row + (col + 1) / 9), (col + 1) % 9):       
                    return True
        puzzle[row][col] = 0
        
    else:
        if solve_puzzle(puzzle, int(row + (col + 1) / 9), (col + 1) % 9):
            return True
    return False