#!/usr/local/bin/python3

import os, sys
import operator

do_small = False


def main():
    input_file = get_input_filename(do_small)

    with open(input_file) as f:
        input = [int(x) for x in f.read().split(',')]

    ans1 = solve(input)
    print(f'Part 1: {ans1}')

    ans2 = 0
    for noun in range(0, 100):
        for verb in range(0, 100):
            ans2 = solve(input, noun, verb)
            if ans2 == 19690720:
                print(f'Part 2: {100 * noun + verb}')
                sys.exit

def addi(inputs, idx, operator):
    register = inputs.copy()
    A, B, C = inputs[idx+1:idx+4]

    register[C] = operator(register[A], register[B])
    return register

def solve(inputs, addr_1 = 12, addr_2 = 2):
    inputs[1] = addr_1
    inputs[2] = addr_2
    opcode_idx = 0
    opcode = inputs[opcode_idx]
    while opcode != 99:
        if opcode == 1:
            op = operator.add
        elif opcode == 2:
            op = operator.mul
        else:
            print("Unkonwn opcode")
            sys.exit()

        inputs = addi(inputs, opcode_idx, op)
        opcode_idx += 4
        opcode = inputs[opcode_idx]
    return inputs[0]


def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
