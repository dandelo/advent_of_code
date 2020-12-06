#!/usr/local/bin/python3

import os

def main():
    input_file = get_input_filename()

    with open(input_file) as f:
        data = f.read()

    ans1 = solve1(data)
    print(f'Part 1 answer: {ans1}')

    ans2 = solve2(data)
    print(f'Part 2 answer: {ans2}')


def solve1(data):
    answer_sets = [set(declaration_form.replace('\n', '')) for declaration_form in data.split('\n\n')]
    return sum([len(x) for x in answer_sets])

def solve2(data):
    answer_sets = [declaration_form.split('\n') for declaration_form in data.split('\n\n')]
    common_answer_count = 0
    for answer_set in answer_sets:
        common_answer_count += len(set.intersection(*map(set,answer_set)))
    return common_answer_count

def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file

if __name__ == '__main__':
    main()
