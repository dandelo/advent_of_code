#!/usr/local/bin/python3

import os
from parse import parse


def main():
    print(f'Part 1 answer: {solve_part1()}')
    print(f'Part 2 answer: {solve_part2()}')


def solve_part1():
    memory = {}
    with open(get_input_filename()) as f:
        for line in f.readlines():
            if line.startswith('mask'):
                mask = parse('mask = {}\n', line)[0]
            else:
                addr, value = parse('mem[{:d}] = {:d}', line)
                result = apply_mask(mask, value)
                memory[addr] = result
    return sum(memory.values())

def solve_part2():
    memory = {}
    with open(get_input_filename()) as f:
        for line in f.readlines():
            if line.startswith('mask'):
                mask = parse('mask = {}\n', line)[0]
            else:
                addr, value = parse('mem[{:d}] = {:d}', line)
                result = apply_mask(mask, value)
                memory[addr] = result
                # print(f'applying value {result} to address {addr}')
    return sum(memory.values())     


def apply_mask(mask, value):
    andMask = int(mask.replace('X', '1'), 2)
    orMask = int(mask.replace('X', '0'), 2)
    
    return (value & andMask) | orMask

def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file


if __name__ == '__main__':
    main()
