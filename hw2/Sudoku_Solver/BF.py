# brute-force

import copy

def validate_puzzle(puzzle):
    for i in range(9):
        temp_row_candidates = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
        temp_col_candidates = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if puzzle[i][j] in temp_row_candidates: 
                temp_row_candidates.remove(puzzle[i][j])
            if puzzle[j][i] in temp_col_candidates:
                temp_col_candidates.remove(puzzle[j][i])
        if len(temp_row_candidates) != 0:
            return False
        if len(temp_col_candidates) != 0:
            return False

    for block_offset_row in range(3):
        for block_offset_col in range(3):
            temp_candidates = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
            for r in range(3):
                for c in range(3):
                    if puzzle[block_offset_row*3 + r][block_offset_col*3 + c] in temp_candidates:
                        temp_candidates.remove(puzzle[block_offset_row*3 + r][block_offset_col*3 + c])
    if len(temp_row_candidates) != 0:
        return False
    
    return True 


def solve_puzzle(puzzle, row, col):
    if row > 8:
        if validate_puzzle(puzzle):
            print("[result] Solution found!\n")
            print(puzzle)
            return True
        return False

    if puzzle[row][col] != 0:
        return solve_puzzle(copy.copy(puzzle), int(row + (col + 1) / 9), (col + 1) % 9)
    
    else: 
        for i in range(1, 10):
            pass_puzzle = copy.copy(puzzle)
            pass_puzzle[row][col] = i
            if solve_puzzle(pass_puzzle, int(row + (col + 1) / 9), (col + 1) % 9):
                return True