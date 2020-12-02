import os
import sys
from itertools import cycle, accumulate


def main():
    input_file = get_input_filename()
    with open(input_file) as f:
        input = f.read().splitlines()
    input = [int(x) for x in input[0]]

    solve1(input)
    solve2(input)


def solve1(input):
    pattern = [0, 1, 0, -1]
    phase_count = 100

    numbers = input
    for _ in range(phase_count):
        next_numbers = []
        for i in range(len(numbers)):
            next_phase_digit = 0
            pattern_repeater = [val for val in pattern for _ in range(i+1)]
            pattern_cycle = cycle(pattern_repeater)
            next(pattern_cycle)
            for digit in numbers:
                next_phase_digit += digit * next(pattern_cycle)
            next_numbers.append(abs(next_phase_digit) % 10)
        numbers = next_numbers
    print(''.join(str(x) for x in numbers))
    print(''.join(str(x) for x in numbers[:8]))

def solve2(input):
    pattern = [0, 1, 0, -1]
    phase_count = 100

    offset = int(''.join(str(x) for x in input[:7]))
    numbers = (10000*input)[offset:]
    for _ in range(phase_count):
        next_numbers = []
        for i in range(len(numbers)):
            next_phase_digit = 0
            pattern_repeater = [val for val in pattern for _ in range(i+1)]
            pattern_cycle = cycle(pattern_repeater)
            next(pattern_cycle)
            for digit in numbers:
                next_phase_digit += digit * next(pattern_cycle)
            next_numbers.append(abs(next_phase_digit) % 10)
        numbers = next_numbers
    print(''.join(str(x) for x in numbers))
    print(''.join(str(x) for x in numbers[:8]))



def get_input_filename(do_small = False):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file


if __name__ == '__main__':
    main()
