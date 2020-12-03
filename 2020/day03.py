#!/usr/local/bin/python3

from parse import parse
import os

def main():
    do_small = False
    input_file = get_input_filename(do_small)

    slope2 = solve(input_file, 3, 1)
    print(f'Part 1 answer: {slope2}')

    slope1 = solve(input_file, 1, 1)
    slope3 = solve(input_file, 5, 1)
    slope4 = solve(input_file, 7, 1)
    slope5 = solve(input_file, 1, 2)
    print(f'Part 2 answer: {slope1 * slope2 * slope3 * slope4 * slope5}')

def solve(input_file, right, down):
    trees_hit = 0
    with open(input_file) as f:
        line_no = 0
        while True:
            if line_no != 0:
                for i in range(down - 1): 
                    f.readline()
            line = f.readline().strip()
            if not line:
                break
            col = line_no*right % len(line)
            tree_or_not = line[col]
            if tree_or_not == '#':
                trees_hit += 1
            line_no += down

    return trees_hit
                    

def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
