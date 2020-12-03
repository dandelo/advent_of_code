#!/usr/local/bin/python3

import os

def main():
    input_file = get_input_filename()

    with open(input_file) as f:
        input = [int(x) for x in f.read().splitlines()]

    ans1 = solve_part1(input)
    print(f'Part 1 answer: {ans1}')

    ans2 = solve_part2(input)
    print(f'Part 2 answer: {ans2}')

def solve_part1(input):
    for i,x in enumerate(input):
        if x > 2020:
            continue
        for y in input[i+1:]:
            if x + y == 2020:
                return x*y
    

def solve_part2(input):
    for i, x in enumerate(input):
        for j, y in enumerate(input[i+1:]):
            for z in input[i+j+1:]:
                if x + y + z == 2020:
                    return x*y*z
                    

def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file

if __name__ == '__main__':
    main()
