#!/usr/local/bin/python3

import os, sys
from parse import parse
from itertools import islice, zip_longest
from collections import defaultdict

do_small = False


def main():
    input_file = get_input_filename(do_small)

    inputs = []

    with open(input_file) as f:
        for line1,line2,line3,line4 in zip_longest(*[f]*4):
            inputs.append(parse_inputs(line1,line2,line3,line4))

    ans = solve(inputs)
    ans1 = [k for k,v in ans.items() if len(v) >= 3]
    print(f'Part 1: {len(ans1)}')

    ans2 = solve_part2(inputs)
    print(f'Part 1: {ans2}')


def addr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = register[A] + register[B]
    is_valid = register == output
    return is_valid, register

def addi(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = register[A] + B
    is_valid = register == output
    return is_valid, register

def mulr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = register[A] * register[B]
    is_valid = register == output
    return is_valid, register

def muli(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = register[A] * B
    is_valid = register == output
    return is_valid, register

def banr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = register[A] & register[B]
    is_valid = register == output
    return is_valid, register

def bani(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = register[A] & B
    is_valid = register == output
    return is_valid, register

def borr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = register[A] | register[B]
    is_valid = register == output
    return is_valid, register

def bori(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = register[A] | B
    is_valid = register == output
    return is_valid, register

def setr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = register[A]
    is_valid = register == output
    return is_valid, register

def seti(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = A
    is_valid = register == output
    return is_valid, register

def gtir(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = 1 if A > register[B] else 0
    is_valid = register == output
    return is_valid, register

def gtri(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = 1 if register[A] > B else 0
    is_valid = register == output
    return is_valid, register

def gtrr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = 1 if register[A] > register[B] else 0
    is_valid = register == output
    return is_valid, register

def eqir(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = 1 if A == register[B] else 0
    is_valid = register == output
    return is_valid, register

def eqri(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = 1 if register[A] == B else 0
    is_valid = register == output
    return is_valid, register

def eqrr(inputs):
    register = inputs[0].copy()
    instruction = inputs[1]
    output = inputs[2]
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]

    register[C] = 1 if register[A] == register[B] else 0
    is_valid = register == output
    return is_valid, register

def solve(inputs):
    OPERATIONS = [
        addr, addi,
        mulr, muli,
        banr, bani,
        borr, bori,
        setr, seti,
        gtir, gtri, gtrr,
        eqir, eqri, eqrr
    ]
    ans = defaultdict(list)
    for i, input_set in enumerate(inputs):
        for operation in OPERATIONS:
            is_valid, output = operation(input_set)
            if is_valid:
                ans[i].append(operation.__name__)
    return (ans)

def solve_part2(inputs):
    OPERATIONS = [
        addr, addi,
        mulr, muli,
        banr, bani,
        borr, bori,
        setr, seti,
        gtir, gtri, gtrr,
        eqir, eqri, eqrr
    ]
    ans = defaultdict(set)
    for input_set in inputs:
        opcode = input_set[1][0]
        for operation in OPERATIONS:
            is_valid, output = operation(input_set)
            if is_valid:
                ans[opcode].add(operation.__name__)

    opscodes = defaultdict(str)
    while len(opscodes) < 16:
        for k,v in ans.items():
            for opscode in opscodes.values():
                v.discard(opscode)
                ans[k] = v
            if len(v) == 1:
                opscodes[k] = v.pop()
    # print(opscodes)

    registers = [0,0,0,0]
    with open('inputs/day16.input.p2') as f:
        test_data = f.read().splitlines()

    test_data_input = []
    for data in test_data:
        test_data_input.append(list(map(int, data.split())))

    for test_step in test_data_input:
        operation = opscodes[test_step[0]]
        # print(operation + '([registers, test_step, []])')
        is_valid, output = eval(operation + '([registers, test_step, []])')
        registers = output
    

    return (registers)


def parse_inputs(line1,line2,line3,line4):
    line1 = list(parse('Before: [{:d}, {:d}, {:d}, {:d}]', line1))
    line2 = list(map(int, line2.split()))
    line3 = list(parse('After:  [{:d}, {:d}, {:d}, {:d}]', line3))
    return [line1,line2,line3]


def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
