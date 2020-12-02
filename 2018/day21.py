#!/usr/local/bin/python3

import os, sys
from itertools import islice, zip_longest

do_small = False
debug = False


def main():
    input_file = get_input_filename(do_small)

    inputs = []
    with open(input_file) as f:
        for line in f.readlines():
            if line[0:3] == "#ip":
                ip_idx = int(line[line.find(" "):])
            else:
                pieces = line.strip().split(" ")
                instructions = [pieces[0]]
                instructions.extend([int(c) for c in pieces[1:]])
                inputs.append(instructions)

    ans1 = solve(inputs, ip_idx)
    print(f'Part 1: {ans1}')

    # ans2 = solve_part2(inputs, ip_idx)
    ans2 = solve(inputs, ip_idx, False)
    print(f'Part 2: {ans2}')


def addi(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A] + B
    return register

def addr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A] + register[B]
    return register

def bani(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A] & B
    return register

def bori(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A] | B
    return register

def borr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A] | register[B]
    return register

def eqri(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = 1 if register[A] == B else 0
    return register

def eqrr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = 1 if register[A] == register[B] else 0
    if register[C] == 1:
        print(register, instruction)
    return register

def gtir(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = 1 if A > register[B] else 0
    return register

def gtrr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = 1 if register[A] > register[B] else 0
    return register

def muli(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A] * B
    return register

def seti(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = A
    return register

def setr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A]
    return register

def solve(inputs, ip_idx, part1=True):
    steps = 0
    registers = [0, 0, 0, 0, 0, 0]
    seen_vals = set()
    last_val = 0
    while True:

        input_set = inputs[registers[ip_idx]]
        op = input_set[0]
        instructions = input_set[1:]
        registers = eval(op + '([registers, instructions, []])')

        # eqrr only op that affects register[0]
        if op == 'eqrr':
            val = registers[instructions[0]]
            if part1:
                return val
            else:
                if val in seen_vals:
                    return last_val
                else:
                    seen_vals.add(val)
                    last_val = val
                    if debug:
                        print(seen_vals)

        registers[ip_idx] += 1
        steps += 1
    return registers[0]

def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
