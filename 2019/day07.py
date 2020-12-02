#!/usr/local/bin/python3
import os
import itertools

do_small = True
last_output = 0
phase_settings = [9,8,7,6,5]
current_phase_settings = [9,8,7,6,5]
is_first_input = True
current_amp = 0
max_output = 0

def main():
    input_file = get_input_filename(do_small)

    with open(input_file) as f:
        input = [int(x) for x in f.read().split(',')]

    solve(input)
    print(f'max output: {max_output}')


def param_accessor(instruction, position):
    opcode_digits = 2
    instruction_padded = f'0000{instruction}'
    if instruction_padded[-opcode_digits - position] == "1":
        return lambda pointer, opcodes: opcodes[pointer+position]
    else:
        return lambda pointer, opcodes: opcodes[opcodes[pointer+position]]


def solve(opcodes):
    global last_output
    global is_first_input
    global current_amp
    global phase_settings
    global current_phase_settings
    amps = ['A', 'B', 'C', 'D', 'E']
    for phase in list(itertools.permutations(phase_settings)):
    # for phase in [[4,3,2,1,0]]:
        last_output = 0
        print(f'phase setting: {phase}')
        current_phase_settings = phase
        current_amp = 0
        for amp in amps:
            is_first_input = True
            pointer = 0
            while pointer is not None:
                instruction = str(opcodes[pointer])
                # print(f'instruction: {instruction}')
                first_param = param_accessor(instruction, 1)
                second_param = param_accessor(instruction, 2)
                if len(instruction) > 2:
                    instruction = instruction[-1]
                pointer = OPERATIONS[instruction](pointer, opcodes, first_param, second_param)
            current_amp += 1


def op_sum(pointer, opcodes, first_param, second_param):
    opcodes[opcodes[pointer+3]] = first_param(pointer, opcodes) + second_param(pointer, opcodes)
    return pointer + 4


def op_mul(pointer, opcodes, first_param, second_param):
    opcodes[opcodes[pointer+3]] = first_param(pointer, opcodes) * second_param(pointer, opcodes)
    return pointer + 4


def op_input(pointer, opcodes, *_):
    global is_first_input

    if is_first_input:
        input = current_phase_settings[current_amp]
        is_first_input = False
    else:
        input = last_output

    # print(f'input is: {input}')
    opcodes[opcodes[pointer+1]] = input

    return pointer + 2


def op_output(pointer, opcodes, first_param, _):
    global last_output
    global max_output
    output = opcodes[opcodes[pointer+1]]
    print(f"output: {output}")
    if output > max_output:
        max_output = output
    last_output = output
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


def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file


if __name__ == '__main__':
    main()
