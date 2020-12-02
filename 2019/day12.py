import os
from parse import parse
import itertools
import copy
from math import gcd
from functools import reduce


def main():
    input_file = get_input_filename()
    moon_coords = list(parse('<x={:d}, y={:d}, z={:d}>', line) for line in open(input_file))
    moon_coord_vel = [{"pos" : list(coord), "vel" : [0,0,0]} for coord in moon_coords]
    # moved_moon_coord_vel = solve(copy.deepcopy(moon_coord_vel))
    # ans = 0
    # for moon in moved_moon_coord_vel:
    #     pot = sum(abs(pos) for pos in moon["pos"])
    #     kin = sum(abs(vel) for vel in moon["vel"])
    #     ans += pot * kin
    # print(ans)

    ans2 = solve2(copy.deepcopy(moon_coord_vel))
    print(ans2)


def solve(moon_coord_vel):
    moon_coord_vel_copy = copy.deepcopy(moon_coord_vel)
    steps = 1000
    for step in range(steps):
        for idx, moon in enumerate(moon_coord_vel_copy):
            vel_change = get_new_pos(moon["pos"], [moon["pos"] for moon in moon_coord_vel_copy])
            moon_coord_vel_copy[idx]["vel"] = [x + y for x, y in zip(moon_coord_vel_copy[idx]["vel"], vel_change)]
        for idx, moon in enumerate(moon_coord_vel_copy):
            moon_coord_vel_copy[idx]["pos"] = [x + y for x, y in zip(moon_coord_vel_copy[idx]["pos"], moon_coord_vel_copy[idx]["vel"])]
        # [print(x) for x in moon_coord_vel_copy]
    return moon_coord_vel_copy

def step(moons):
    for idx, moon in enumerate(moons):
        vel_change = get_new_pos(moon["pos"], [moon["pos"] for moon in moons])
        moon_coord_vel_copy[idx]["vel"] = [x + y for x, y in zip(moons[idx]["vel"], vel_change)]
    for idx, moon in enumerate(moons):
        moon_coord_vel_copy[idx]["pos"] = [x + y for x, y in zip(moons[idx]["pos"], moons[idx]["vel"])]

def solve2(moons):
    steps = 0
    # initial_state = tuple(itertools.chain.from_iterable([moon_pos for moon_pos in [moon["pos"] + moon["vel"] for moon in moon_coord_vel]]))

    period =  dict()
    start = [[(m.pos[axis], m.vel[axis]) for m in moons] for axis in range(3)]

    while len(period) < 3:
        steps += 1
        step(moons)

        for axis in range(3):
            '''
            See if current (pos_axis, vel_axis) for all moons match their starting values:
            '''
            if axis not in period and start[axis] == [(m.pos[axis], m.vel[axis]) for m in moons]: 
                period[axis] = steps

        print('After', steps, 'steps:')
        print('ans:', reduce(lcm, period.values()))

    return reduce(lcm, period.values())

def get_new_pos(moon_coord, moon_coords):
    new_vel = [0,0,0]
    for coord in moon_coords:
        if coord == moon_coord:
            continue
        for idx, axis in enumerate(coord):
            if axis > moon_coord[idx]:
                new_vel[idx] += 1
            elif axis < moon_coord[idx]:
                new_vel[idx] -= 1
    return new_vel


def get_input_filename(do_small = False):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

def lcm(a, b):
  return (a * b) // gcd(a, b)

if __name__ == '__main__':
    main()
