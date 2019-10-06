# forword-checking with Mininum Remaining Values(MRV) heuristics

class grid:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.block = find_block(row, col)
        self.number = 0
        self.remain_values = set()

    def set_number(self, number):
        self.number = number
    
    def set_value(self, values):
        self.remain_values = values


    def __lt__(self, other):
        if len(self.remain_values) < len(other.remain_values):
            return True

def find_block(row, col):
    if 0 <= row < 3:
        if 0 <= col < 3:
            return 0
        elif 3 <= col < 6:
            return 1
        else:
            return 2
    elif 3 <= row < 6:
        if 0 <= col < 3:
            return 3
        elif 3 <= col < 6:
            return 4
        else:
            return 5
    else: 
        if 0 <= col < 3:
            return 6
        elif 3 <= col < 6:
            return 7
        else:
            return 8

def init_grids(puzzle):
    grids = []
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                grids.append(grid(i, j))
    return grids

def init_rows(puzzle):
    rows = []
    for i, row in enumerate(puzzle):
        numset = set()
        for num in row:
            if num != 0:
                numset.add(num)
        rows.append(numset)
    return rows

def init_cols(puzzle):
    cols = []
    for i in range(9):
        numset = set()
        for j in range(9):
            if puzzle[j][i] != 0:
                numset.add(puzzle[j][i])
        cols.append(numset)
    return cols

def init_blocks(puzzle):
    blocks = []
    for _ in range(9):
        blocks.append(set())
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                block = find_block(i, j)
                blocks[block].add(puzzle[i][j])
    return blocks

def update_set(rows, cols, blocks, grid, is_add):
    if is_add:
        rows[grid.row].add(grid.number)
        cols[grid.col].add(grid.number)
        blocks[grid.block].add(grid.number)
    else:
        rows[grid.row].discard(grid.number)
        cols[grid.col].discard(grid.number)
        blocks[grid.block].discard(grid.number) 

def reach_goal(rows, cols, blocks):
    for i in range(9):
        if len(rows[i]) != 9 or len(cols[i]) != 9 or len(blocks[i]) != 9:
            return False
    return True

def grid_sort(grids, rows, cols, blocks, num_set):
    for grid in grids:
        remain_values = num_set - (rows[grid.row] | cols[grid.col] | blocks[grid.block])
        if remain_values:
            grid.set_value(remain_values)
        else:
            return False
    grids.sort()
    return True

def solve(grids, rows, cols, blocks, num_set):
    if grid_sort(grids, rows, cols, blocks, num_set):
        grid = grids.pop(0)
        for remain_value in grid.remain_values:
            grid.set_number(remain_value)
            update_set(rows, cols, blocks, grid, True)
            if reach_goal(rows, cols, blocks):
                grids.insert(0, grid)
                return True
            
            else:
                if grids:
                    if solve(grids, rows, cols, blocks, num_set):
                        grids.insert(0, grid)
                        return True
                    else:
                        update_set(rows, cols, blocks, grid, False)
                        grid.set_number(0)
                else:
                    update_set(rows, cols, blocks, grid, False)
                    grid.set_number(0)
        grids.insert(0, grid)
        return False   
    else:
        return False


def solve_puzzle(puzzle):
    rows = init_rows(puzzle)
    cols = init_cols(puzzle)
    blocks = init_blocks(puzzle)
    grids = init_grids(puzzle)

    num_set = {i for i in range(1, 10)}

    if solve(grids, rows, cols, blocks, num_set):
        for grid in grids:
            puzzle[grid.row][grid.col] = grid.number
        return True   
    else:                 
        return False