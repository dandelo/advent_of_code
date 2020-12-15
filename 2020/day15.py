#!/usr/local/bin/python3

import os

def main():
    print(f'Part 1 answer: {solve_better()}')
    print(f'Part 2 answer: {solve_better(30000000)}')

def solve_better(target_number = 2020):
    numbers = (2,0,1,9,5,19)
    last_seen = {}
    for idx, i in enumerate(numbers[:-1]):
        last_seen[i] = idx
    
    next_num = prev_number = numbers[-1]
    for turn in range(len(numbers) - 1, target_number):
        prev_number = next_num
        if next_num not in last_seen:
            last_seen[next_num] = turn
            next_num = 0
        else:
            diff = turn - last_seen[next_num]
            last_seen[next_num] = turn
            next_num = diff
    
    return prev_number

def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file


if __name__ == '__main__':
    main()
