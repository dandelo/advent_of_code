#!/usr/local/bin/python3

import os


def main():
    numbers = [int(line.strip()) for line in open(get_input_filename())]
    invalid_number = solve_part1(numbers, 25)
    print(f'Part 1 answer: {invalid_number}')
    print(f'Part 2 answer: {(solve_part2(numbers, invalid_number))}')

def solve_part1(numbers, preamble_len = 25):
    count = 0
    prev_numbers = numbers[:preamble_len]
    next_num = numbers[preamble_len]
    while True:
        if not is_sumable(next_num, prev_numbers):
            return next_num
        count += 1
        prev_numbers = numbers[count:count+preamble_len]
        next_num = numbers[count+preamble_len]

def solve_part2(numbers, invalid_number):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            list_part = numbers[i:j]
            if invalid_number == sum(list_part):
                return min(list_part) + max(list_part)
            elif sum(list_part) > invalid_number:
                break

def is_sumable(target_number, list):
    for idx, val in enumerate(list):
        if target_number - val in list[idx+1:]:
            return True
    
    return False

def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file

if __name__ == '__main__':
    main()
