#!/usr/local/bin/python3

from operator import itemgetter
from parse import parse, compile
import os
from sys import exit
import numpy as np

np.set_printoptions(linewidth=np.nan, threshold=np.nan)
do_small = False

def main():
    input_file = get_input_filename(do_small)

    # data = []
    # for line in open(input_file):
    #     x,y,vx,vy = map(int, re.findall('-?\d+', line))
    #     data.append([x,y,vx,vy])

    with open(input_file) as f:
        data = list(map(parse_file_line, f))
    data = np.array(data)
    solve(data)

def print_stuff(data):
    min_vals = data.min(0).tolist()
    min_x = min_vals[0]
    min_y = min_vals[1]

    max_vals = data.max(0).tolist()
    max_x = max_vals[0]
    max_y = max_vals[1]
    abs_x = abs(min_x - max_x)
    abs_y = abs(min_y - max_y)

    # print(f'min_x = {min_x}, max_x = {max_x}, abs_x = {abs_x}')
    # print(f'min_y = {min_y}, max_y = {max_y}, abs_y = {abs_y}')

    for i in range(3):
        # print((data[:,0]+i*data[:,2]).max() - (data[:,0]+i*data[:,2]).min())
        x_max = max(data[:,0] + i * data[:,2])
        x_min = min(data[:,0] + i * data[:,2])
        y_max = max(data[:,1] + i * data[:,3])
        y_min = min(data[:,1] + i * data[:,3])
        abs_x = abs(min_x - max_x)
        abs_y = abs(min_y - max_y)
        print(f'min_x = {min_x}, max_x = {max_x}, abs_x = {abs_x}')
        print(f'min_y = {min_y}, max_y = {max_y}, abs_y = {abs_y}')
        # x_len = abs(max(data[:,0] + i * data[:,2]) - min(data[:,0] + i * data[:,2]))
        # y_len = abs(max(data[:,2] + i * data[:,3]) - min(data[:,1] + i * data[:,3]))
        # print(f'x_len = {x_len}, y_len = {y_len}')
        #+i*data[:,2]).max() - (data[:,0]+i*data[:,2]).min())
        # print(Y.append((data[:,1]+i*data[:,3]).max() - (data[:,1]+i*data[:,3]).min()))

def solve(data):
    i = 0
    y_abs = 22

    while y_abs > 10:
        # min_vals = data.min(0).tolist()
        # min_x = min_vals[0]
        # min_y = min_vals[1]
        x_max = max(data[:,0] + i * data[:,2])
        x_min = min(data[:,0] + i * data[:,2])
        y_max = max(data[:,1] + i * data[:,3])
        y_min = min(data[:,1] + i * data[:,3])
        x_abs = abs(x_min - x_max) + 1
        y_abs = abs(y_min - y_max) + 1

        print(f'{i} ({y_abs})')
        if y_abs > 10:
            i += 1
            continue

        sky = np.zeros((x_abs, y_abs), 'U1')
        # sky = np.zeros((x_max + 1, y_max + 1), 'U1')
        sky.fill(' ')

        for pos in data:
            x_pos, y_pos, x_vel, y_vel = pos[:]
            x_pos += (x_vel * i) - x_min
            y_pos += (y_vel * i) - y_min
            # x_pos += (x_vel * i)
            # y_pos += (y_vel * i)
            if x_pos < 0 or y_pos < 0:
                print('ERROR')
                return
            sky[x_pos][y_pos] = '*'
        i += 1
        print_sky(sky)

def print_sky(sky):
    reversed_arr = sky[::-1]
    print((np.rot90(np.rot90(np.rot90(reversed_arr)))))
    # print(np.rot90(np.rot90(np.rot90(sky))))
    # print(sky)

def parse_file_line(line):
    line_els = line.split(',')
    x = map(int, line_els)
    return list(x)


def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
