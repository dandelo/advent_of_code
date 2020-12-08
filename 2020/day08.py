#!/usr/local/bin/python3

from copy import deepcopy
import os

def main():
    with open(get_input_filename()) as f:
        instrutions = [line.split() for line in f]
    
    print(f'Part 1 answer: {solve(instrutions)[0]}')
    print(f'Part 2 answer: {solve_part2(instrutions)}')

def solve_part2(instrutions):
    nop_and_jmp_idxs = [y for y,x in enumerate(instrutions) if x[0] in ['nop', 'jmp']]

    for idx in nop_and_jmp_idxs:
        instrutions_copy = deepcopy(instrutions)
        instrutions_copy[idx][0] = instrutions_copy[idx][0].replace('jmp','-').replace('nop','jmp').replace('-','nop')
        accumulator, success = solve(instrutions_copy)
        
        if success:
            return accumulator
    

def solve(instrutions):
    seen_pointers = set()
    accumulator = pointer = 0

    while True:
        if pointer in seen_pointers:
            return accumulator, False
        elif pointer >= len(instrutions):
            return accumulator, True

        operation = instrutions[pointer][0]
        arg = int(instrutions[pointer][1])

        seen_pointers.add(pointer)

        if operation == 'acc':
            accumulator += arg
        elif operation == 'jmp':
            pointer+=arg
            continue

        pointer+=1


def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file

if __name__ == '__main__':
    main()
