import lib.commons as commons
import numpy as np
from parse import parse

input_file = commons.get_input_filename()
lines = commons.read_file_to_list(input_file)


def draw_line(coord1, coord2, array, count_diag=False):
    hoz_dir = 1 if coord1[0] < coord2[0] else -1
    vert_dir = 1 if coord1[1] < coord2[1] else -1
    x_coords = range(coord1[0], coord2[0]+hoz_dir, hoz_dir)
    y_coords = range(coord1[1], coord2[1]+vert_dir, vert_dir)

    # hor or vert line
    if coord1[0] == coord2[0] or coord1[1] == coord2[1]:
        for x in x_coords:
            for y in y_coords:
                array[x, y] = 1 if array[x, y] == 0 else 2
    # diag line
    elif count_diag:
        for coord in zip(x_coords, y_coords):
            array[coord] = 1 if array[coord] == 0 else 2


def solve(is_part_two: bool):
    size = 1000
    ocean_floor = np.zeros((size, size))
    for line in lines:
        x1, y1, x2, y2 = parse("{:d},{:d} -> {:d},{:d}", line)
        draw_line((x1, y1), (x2, y2), ocean_floor, is_part_two)
    # commons.print_like_aoc(ocean_floor)
    print(np.count_nonzero(ocean_floor == 2))


solve(False)
solve(True)
