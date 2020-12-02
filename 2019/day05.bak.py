#!/usr/local/bin/python3

import os, sys
import operator

do_small = False
input = 1

def main():
    input_file = get_input_filename(do_small)

    with open(input_file) as f:
        input = [int(x) for x in f.read().split(',')]

    ans1 = solve(input)

def param_accessor(instruction, position):
    opcode_digits = 2
    instruction_padded = f'0000{instruction}'
    if instruction_padded[-opcode_digits - position] == "1":
        return lambda pointer, opcodes: opcodes[pointer+position]
    else:
        return lambda pointer, opcodes: opcodes[opcodes[pointer+position]]

def solve(opcodes):
    pointer = 0
    while pointer is not None:
        instruction = str(opcodes[pointer])
        print(f'instruction: {instruction}')
        first_param = param_accessor(instruction, 1)
        second_param = param_accessor(instruction, 2)
        if len(instruction) > 2:
            instruction = instruction[-1]
        pointer = OPERATIONS[instruction](pointer, opcodes, first_param, second_param)
    return opcodes

def solve2(opcodes):
    pointer = 0
    # instruction = "0"
    # while True:
    while pointer is not None:
        instruction = str(opcodes[pointer])
        # print(f"instruction: {instruction}")
        # if len(instruction) > 2:
        #     second_param_mode, first_param_mode = map(int, f'0000{instruction}'[-4:-2])
        #     first_param, second_param = opcodes[pointer+1:pointer+3]
        #     if first_param_mode == 0:
        #         first_param = opcodes[first_param]
        #     if second_param_mode == 0:
        #         second_param = opcodes[second_param]
        #     instruction = str(opcodes[pointer])[-1]

        # else:
        #     first_param, second_param = opcodes[pointer+1: pointer+3]
        #     first_param = opcodes[first_param]
        #     second_param = opcodes[second_param]


        # pointer = OPERATIONS[instruction](pointer, opcodes, first_param, second_param)

        first_param = param_accessor(instruction, 1)
        second_param = param_accessor(instruction, 2)
        pointer = OPERATIONS[instruction[-1]](pointer, opcodes, first_param, second_param)
    return opcodes

def op_sum(pointer, opcodes, first_param, second_param):
    opcodes[opcodes[pointer+3]] = first_param(pointer, opcodes) + second_param(pointer, opcodes)
    return pointer + 4


def op_mul(pointer, opcodes, first_param, second_param):
    opcodes[opcodes[pointer+3]] = first_param(pointer, opcodes) * second_param(pointer, opcodes)
    return pointer + 4


def op_input(pointer, opcodes, *_):
    print(f'{opcodes[opcodes[pointer+1]]} = 1')
    opcodes[opcodes[pointer+1]] = input
    return pointer + 2


def op_output(pointer, opcodes, first_param, _):
    print(f"result: {opcodes[opcodes[pointer+1]]}")
    return pointer + 2


def op_jump_if_true(pointer, opcodes, first_param, second_param):
    if first_param(pointer, opcodes) != 0:
        return second_param(pointer, opcodes)
    return pointer + 3


def op_jump_if_false(pointer, opcodes, first_param, second_param):
    if first_param(pointer, opcodes) == 0:
        return second_param(pointer, opcodes)
    return pointer + 3


def op_less_than(pointer, opcodes, first_param, second_param):
    opcodes[opcodes[pointer+3]] = 1 if first_param(pointer, opcodes) < second_param(pointer, opcodes) else 0
    return pointer + 4


def op_equal(pointer, opcodes, first_param, second_param):
    opcodes[opcodes[pointer+3]] = 1 if first_param(pointer, opcodes) == second_param(pointer, opcodes) else 0
    return pointer + 4

def exit(*_):
    return None

OPERATIONS = {
    "1": op_sum,
    "2": op_mul,
    "3": op_input,
    "4": op_output,
    "5": op_jump_if_true,
    "6": op_jump_if_false,
    "7": op_less_than,
    "8": op_equal,
    "99": exit,
}

# def addi(inputs, idx, operator):
#     register = inputs.copy()
#     opcode = f'{inputs[idx]:06}'
#     mode1 = int(opcode[-3])
#     mode2 = int(opcode[-4])
#     mode3 = int(opcode[-5])

#     A, B, C = inputs[idx+1:idx+4]

#     if mode1 == 0:
#         A = register[A]
#     elif mode1 != 1:
#         print(f"Error unknown mode {mode1}")
#     if mode2 == 0:
#         B = register[B]
#     elif mode2 != 1:
#         print(f"Error unknown mode {mode2}")

#     if mode3 == 1:
#         C = register[C]
#     elif mode3 != 0:
#         print(f"Error unknown mode {mode3}")



#     register[C] = operator(A, B)
#     return register

# def inout(program, opcode_idx, op, input = 5):
#     address = program[opcode_idx+1]
#     if op == "input":
#         program[address] = input
#     elif op == "output":
#         print(program[address])
#     return program

# def solve(program):
#     pointer = 0
#     opcode = program[pointer]
#     while opcode != 99:
#         instruction_count = 4
#         function = "addi"
#         opcode = int(str(opcode)[-1])
#         if opcode == 1:
#             op = operator.add
#         elif opcode == 2:
#             op = operator.mul
#         elif opcode == 3:
#             instruction_count = 2
#             function = "inout"
#             op = "input"
#         elif opcode == 4:
#             instruction_count = 2
#             function = "inout"
#             op = "output"
#         elif opcode == 5:
#             instruction_count = 3
#             if program[pointer+1] != 0:
#                 pointer = program[pointer+2]
#                 opcode = program[pointer]
#             else:
#                 pointer += instruction_count
#                 opcode = program[pointer]
#             continue
#         elif opcode == 6:
#             instruction_count = 3
#             if program[pointer+1] == 0:
#                 pointer = program[pointer+2]
#                 opcode = program[pointer]
#             else:
#                 pointer += instruction_count
#                 opcode = program[pointer]
#             continue
#         elif opcode == 7:
#             if program[pointer+1] < program[pointer+2]:
#                 to_store = 1
#             else:
#                 to_store = 0
#             program[pointer+3] = to_store
#             pointer += instruction_count
#             opcode = program[pointer]
#             continue
#         elif opcode == 8:
#             if program[pointer+1] == program[pointer+2]:
#                 to_store = 1
#             else:
#                 to_store = 0
#             program[pointer+3] = to_store
#             pointer += instruction_count
#             opcode = program[pointer]
#             continue
#         else:
#             print("Unkonwn opcode")
#             sys.exit()

#         program = eval(function + '(program, pointer, op)')
#         # program = addi(program, opcode_idx, op)
#         pointer += instruction_count
#         opcode = program[pointer]
#     return program


def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
