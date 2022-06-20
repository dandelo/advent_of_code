import lib.commons as commons
import statistics

input_file = commons.get_input_filename()
input = commons.read_file_to_list(input_file)
open_chars = '[{(<'
close_chars = ']})>'
open_close_mapper = {
    '[': ']',
    '{': '}',
    '(': ')',
    '<': '>',
}


def part_one(input):
    illegal_char_point_mapper = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    first_illegal_chars = []

    for line in input:
        openers = []
        for char in line:
            if char in open_chars:
                openers.append(char)
            elif char in close_chars:
                last_opener = openers.pop()
                if open_close_mapper[last_opener] != char:
    #                 print(f"Expected {open_close_mapper[last_opener]}, but found {char} instead.")
                    first_illegal_chars.append(char)
                    break
            else:
                raise Exception(f"unknown character found: '{char}'")

    points = 0
    for char in first_illegal_chars:
        points += illegal_char_point_mapper[char]
    return points


def part_two(input):
    missing_char_point_mapper = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    incomplete_lines = []

    for line in input:
        openers = []
        line_is_corrupt = False
        for char in line:
            if char in open_chars:
                openers.append(char)
            elif char in close_chars:
                last_opener = openers.pop()
                if open_close_mapper[last_opener] != char:
                    line_is_corrupt = True
                    break
            else:
                raise Exception(f"unknown character found: '{char}'")
        if not line_is_corrupt:
            incomplete_lines.append(openers)

    points = []
    for line in incomplete_lines:
        line_points = 0
        line.reverse()
        for char in line:
            missing_char = open_close_mapper[char]
            line_points = line_points * 5 + missing_char_point_mapper[missing_char]
        points.append(line_points)
    
    return statistics.median(points)


print(part_one(positions))
print(part_two(positions))
