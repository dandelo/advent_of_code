import lib.commons as commons
import numpy as np
from parse import parse
import math

input_file = commons.get_input_filename()
coords = []
instructions = []
with open(input_file) as myfile:
    read_all_coords = False
    for line in myfile:
        line = line.strip()
        if line == '':
            read_all_coords = True
            continue
        if not read_all_coords:
            coord = [int(x) for x in line.split(',')]
            coords.append(coord)
        else:
            instructions.append(line)

x_len = max(coord[0] for coord in coords) + 1
y_len = max(coord[1] for coord in coords) + 1

# paper may not have # at last line, so make sure paper length is odd to allow fold
x_len = 2*math.floor(x_len/2)+1
y_len = 2*math.floor(y_len/2)+1

paper = np.full((x_len, y_len), '.', dtype='U1')
for coord in coords:
    paper[coord[0], coord[1]] = '#'


def fold_paper(paper, axis, fold_at):
    if axis == 1:
        half_one = paper[:, :fold_at]
        half_two = np.flip(paper[:, fold_at+1:], axis=axis)
    else:
        half_one = paper[:fold_at, :]
        half_two = np.flip(paper[fold_at+1:, :], axis=axis)
    # Add half_two to half_one
    half_two_hashes = half_two == '#'
    half_one[half_two_hashes] = '#'
    return half_one


def part_one(paper):
    instruction = instructions[0]
    axis, value = parse('fold along {}={:d}', instruction)
    axis = int(axis == 'y')
    paper = fold_paper(paper, axis, value)
    return sum(sum(paper == '#'))


def part_two(paper):
    for instruction in instructions:
        axis, value = parse('fold along {}={:d}', instruction)
        axis = int(axis == 'y')
        paper = fold_paper(paper, axis, value)

    return paper


print(part_one(paper))
np.set_printoptions(linewidth=200)
commons.print_like_aoc(part_two(paper))
