#!/usr/local/bin/python3

from operator import itemgetter
from parse import parse, compile
import os
from sys import exit
import numpy as np

do_small = False

if do_small:
    initial_state = '#..#.#..##......###...###'
else:
    initial_state = '####..##.##..##..#..###..#....#.######..###########.#...#.##..####.###.#.###.###..#.####..#.#..##..#'

def main():
    input_file = get_input_filename(do_small)

    with open(input_file) as f:
        data = f.read().splitlines()

    plant_spawn_config = get_create_plants(data)

    ans = solve(plant_spawn_config)
    print(ans)

    ans = solve(plant_spawn_config, False)
    print(ans)


def solve(mappings, part_1 = True):
    if part_1:
        generation_count = 20
    else:
        generation_count = 50000000000
    zero_idx = sum = 0
    next_gen = initial_state
    for generation in range(generation_count):
        if generation >= 1000:
            sum +=  (generation_count - 1000) * 88
            break
        zero_idx, current_gen = make_current_gen(zero_idx, next_gen)
        # print(current_gen)
        next_gen = ''
        gen_size = len(current_gen)
        for i in range(gen_size):
            if i == 0:
                plants = '..' + ''.join(current_gen[i:(i+3)])
            elif i == 1:
                plants = '.' + ''.join(current_gen[(i-1):(i+3)])
            elif i == gen_size - 2:
                plants = ''.join(current_gen[(i-2):(i+2)]) + '.'
            elif i == gen_size - 1:
                plants = ''.join(current_gen[(i-2):(i+1)]) + '..'
            else:
                plants = current_gen[(i-2):(i+3)]
            nex_gen_plant = get_nex_gen_plant(plants, mappings)
            next_gen += nex_gen_plant
        current_gen = next_gen
        sum = count_plants(zero_idx, current_gen)
        print(f'gen {generation} = {sum}')

    print(current_gen)
    # sum = count_plants(zero_idx, current_gen)
    return sum

def count_plants(zero_idx, current_gen):
    sum = 0
    for i, plant in enumerate(current_gen):
        if plant == '#':
            sum += i - zero_idx
    return sum

def make_current_gen(zero_idx, gen):
    gen_size = len(gen)
    first_plant_idx = gen.find('#')
    last_plant_idx = gen.rfind('#')

    if first_plant_idx == 0:
        gen = '..' + gen
        zero_idx += 2
    elif first_plant_idx == 1:
        gen = '.' + gen
        zero_idx +=1

    if last_plant_idx == gen_size - 2:
        gen += '.'
    elif last_plant_idx == gen_size - 1:
        gen += '..'

    return zero_idx, gen


def get_nex_gen_plant(plants, mappings):
    if plants in mappings:
        return '#'
    else:
        return '.'

def get_create_plants(all):
    creates_plants = []
    for line in all:
        plants, is_plant = parse('{} => {}', line)
        if is_plant == '#':
            creates_plants.append(plants)
    return creates_plants

def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
