# This Python Program solve the Sudoku problem by using following three method:
# 1. brute force method (exhaustive search)
# 2. back-tracking (Constraint Satisfaction Problem, CSP) 
# 3. forword-checking with Mininum Remaining Values(MRV) heuristics

# 文件读取时，需要先进入本程序所在的文件目录下

import os
import sys
import time
import copy
import numpy as np
import BF
import BT
import MRV

testcase_dir = "testCases"
solution_dir = "solutions"
performance_dir = "performances"


def validate_args(argv):
    if len(argv) < 3 or len(argv) > 3:
        sys.exit('[Error] Except two argument: <filename> <method>') 

def read_file(filename):
    puzzle = []
    with open(os.path.join(testcase_dir, filename), 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            puzzle.append([int(i) for i in line.split()])
    return np.array(puzzle)

def write_file(filename):
    pass


def load_puzzle(filename):
    return np.loadtxt(os.path.join(testcase_dir, filename), dtype=int)

def save_solution(filename, solution):
    np.savetxt(os.path.join(solution_dir, filename), solution, fmt="%d")

def solve(puzzle, method):
    if method == "BF":
        return BF.solve_puzzle(copy.copy(puzzle), 0, 0)
    elif method == "BT":
        return BT.solve_puzzle(puzzle, 0, 0)
    elif method == "FC-MRV":
        return MRV.solve_puzzle(puzzle)
    else:
        sys.exit('[Error] This program only provide two method: BF, BT or FC-MRV') 

def main(argv):
    program_start_time = time.time()
    validate_args(argv)

    testcase_file = argv[1]
    solution_file = "solution" + argv[1][6] + ".txt"
    
    # load puzzle
    print("\n[status] Loading puzzle...\n")
    puzzle = load_puzzle(testcase_file)
    
    print("[Status] Solving the puzzle...\n")
    method_start_time = time.time()
    if solve(puzzle, argv[2]):
        method_end_time = time.time()
        if(argv[2] != "BF"):
            print("[result] Solution found!\n")
            print(puzzle)

        #save result
        save_solution(solution_file, puzzle)

        program_end_time = time.time()
        
        print("\n[Performance] Total time the Program cost: %.3fs" % (program_end_time - program_start_time))
        print("              Total time the solver cost: %.3fs" % (method_end_time - method_start_time))
    else:
        print("[Error] No solution")
    

if __name__ == "__main__":
    main(sys.argv)