#!/usr/local/bin/python3

import os, sys
from itertools import islice, zip_longest

do_small = False
debug = True


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

    # ans1 = solve(inputs, 0, ip_idx)
    # print(f'Part 1: {ans1}')

    ans2 = sum(solve2())
    print(f'Part 2: {ans2}')


def addr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A] + register[B]
    return register

def addi(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A] + B
    return register

def mulr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A] * register[B]
    return register

def muli(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A] * B
    return register

def banr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A] & register[B]
    return register

def bani(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A] & B
    return register

def borr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A] | register[B]
    return register

def bori(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A] | B
    return register

def setr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = register[A]
    return register

def seti(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = A
    return register

def gtir(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = 1 if A > register[B] else 0
    return register

def gtri(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = 1 if register[A] > B else 0
    return register

def gtrr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = 1 if register[A] > register[B] else 0
    return register

def eqir(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    A = instruction[0]
    B = instruction[1]
    C = instruction[2]

    register[C] = 1 if A == register[B] else 0
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
    return register

def solve2(n=10551315):
    max = n
    num = 2
    result = [1, n]

    while num < max:
        if not n % num:
            if num != n/num:
                result.extend([num, n//num])
            else:
                result.append(num)
            max = n//num
        num += 1
    return sorted(result)

def solve(inputs, ip_start, ip_idx):
    steps = 0
    registers = [ip_start, 0, 0, 0, 0, 0]
    while registers[ip_idx] < len(inputs):

        input_set = inputs[registers[ip_idx]]
        op = input_set[0]
        instructions = input_set[1:]
        registers = eval(op + '([registers, instructions, []])')

        if debug:
            if steps % 10000 < 15:
                print(registers, op, instructions)
            if steps % 10000 == 15:
                print()

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
