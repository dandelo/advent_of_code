import lib.commons as commons
import numpy as np

input_file = commons.get_input_filename()
with open(input_file) as myfile:
    octopi = commons.read_file_to_np_array(input_file)


def part_one(octopi, steps):
    x_len = len(octopi)
    y_len = len(octopi[0])
    flashes = 0
    next_step = octopi
    for _ in range(steps):
        flashed_this_turn = []
        next_step = next_step + 1
        for (x, y), item in np.ndenumerate(next_step):
            if item > 9:
                surround = next_step[max(x-1, 0):min(x+2, x_len), max(y-1, 0):min(y+2, y_len)] + 1
                next_step[max(x-1, 0):min(x+2, x_len), max(y-1, 0):min(y+2, x_len)] = surround
                flashed_this_turn.append((x, y))
                flashes += 1
        while len(flashed_this_turn) != (next_step > 9).sum():
            for (x, y), item in np.ndenumerate(next_step):
                if item > 9 and (x, y) not in flashed_this_turn:
                    surround = next_step[max(x-1, 0):min(x+2, x_len), max(y-1, 0):min(y+2, y_len)] + 1
                    next_step[max(x-1, 0):min(x+2, x_len), max(y-1, 0):min(y+2, y_len)] = surround
                    flashed_this_turn.append((x, y))
                    flashes += 1
        next_step = np.where(next_step > 9, 0, next_step)
    return flashes


def part_two(octopi):
    x_len = len(octopi)
    y_len = len(octopi[0])
    next_step = octopi
    steps = 0
    while True:
        flashed_this_turn = []
        next_step = next_step + 1
        for (x, y), item in np.ndenumerate(next_step):
            if item > 9:
                surround = next_step[max(x-1, 0):min(x+2, x_len), max(y-1, 0):min(y+2, y_len)] + 1
                next_step[max(x-1, 0):min(x+2, x_len), max(y-1, 0):min(y+2, x_len)] = surround
                flashed_this_turn.append((x, y))
        while len(flashed_this_turn) != (next_step > 9).sum():
            for (x, y), item in np.ndenumerate(next_step):
                if item > 9 and (x, y) not in flashed_this_turn:
                    surround = next_step[max(x-1, 0):min(x+2, x_len), max(y-1, 0):min(y+2, y_len)] + 1
                    next_step[max(x-1, 0):min(x+2, x_len), max(y-1, 0):min(y+2, y_len)] = surround
                    flashed_this_turn.append((x, y))
        next_step = np.where(next_step > 9, 0, next_step)
        steps += 1
        if len(flashed_this_turn) == np.size(next_step):
            return steps


print(part_one(octopi, 100))
print(part_two(octopi))
