#!/usr/local/bin/python3

from operator import itemgetter
from parse import parse, compile
import os, sys
from sys import exit
import numpy as np
import collections

do_small = False


def main():
    input_file = get_input_filename(do_small)

    with open(input_file) as f:
        tracks = f.read().splitlines()

    trains = get_trains(tracks)
    tracks = remvove_trains(tracks)
    ans = solve(tracks, trains)
    print(ans)


def solve(tracks, trains):
    next_trains = trains.copy()
    # print_tracks_n_trains(tracks, trains)
    counter = 0
    while len(trains) > 1:
        trains = sorted(next_trains, key=lambda element: (element[1],element[0]))
        next_trains = []
        # train_removed = False
        trains_coords = [(x[0]) for x in trains]
        # crash_coords = ()
        crashed_train = []
        for train in trains:
            if train == crashed_train:
                continue
            # if train[0] == crash_coords:
            #     crash_coords = ()
            #     continue
            train_coords, train_vel, train_next_turn = get_moved_train(tracks, train)
            # next_trains.append(train)
            next_trains_coords = [(x[0]) for x in next_trains]
            # train_coords = train[0]

            # if train_coords == crash_coords:
            #     crash_coords = ()
            #     continue
#            if trains_coords.count(train_coords) + next_trains_coords.count(train_coords) > 1:
            if next_trains_coords.count(train_coords) == 1:
                next_trains = [x for x in next_trains if x[0] != train_coords]
            elif trains_coords.count(train_coords) > 1:
                # crash_coords == train_coords
                # crash_coords = train_coords
                crashed_train = [x for x in trains if x[0] == train_coords]
                # trains = [x for x in trains if x[0] != train_coords]
                # next_trains = [x for x in next_trains if x[0] != train_coords]
                # train_removed = True
        # if len(trains) != len(set(trains_coords)):
                # crash_coords = [item for item, count in collections.Counter(trains_coords).items() if count > 1]
                # print_tracks_n_trains(tracks, trains)
                # print(trains)
                # print(counter)
            else:
                next_trains.append([train_coords, train_vel, train_next_turn])
                # return (train_coords[1],train_coords[0]) # (crash_coords[1],crash_coords[0])
        # if crash_coords:
        #     next_trains = [x for x in next_trains if x[0] != crash_coords]
        # next_trains = [x for x in next_trains if x[0] != crash_coords]
        # trains = sorted(next_trains, key=lambda element: (element[1],element[0]))
        # print(trains)
        print(f'{counter} - Trains left: {len(trains)}')
        counter += 1
        # print(trains)
        # print(counter)
        # print_tracks_n_trains(tracks, trains)
    
    return (train_coords[1],train_coords[0]) # (crash_coords[1],crash_coords[0])


def print_tracks_n_trains(tracks, trains):
    this_tracks = tracks.copy()
    for train in trains:
        train_coords = train[0]
        y = train_coords[0]
        x = train_coords[1]
        this_tracks[y] = this_tracks[y][:x] + '*' + this_tracks[y][x+1:]
    print_tracks(this_tracks)

def get_moved_train(tracks,train):
    train_coords = train[0]
    train_vel = train[1]
    train_next_turn = train[2]
    # train_coords = tuple(sum(x) for x in zip(train,train_vel))
    x_coord = train_coords[0] + train_vel[0]
    y_coord = train_coords[1] + train_vel[1]

    next_track = tracks[x_coord][y_coord]
    if next_track in '|-': # Continue straight
        train_vel = train_vel
    elif next_track == '/':
        train_vel = (train_vel[1]*-1,train_vel[0]*-1)
    elif next_track == '\\':
        train_vel = (train_vel[1],train_vel[0])
    elif next_track == '+':
        if train_next_turn == 'L':
            if train_vel == (1,0):
                train_vel = (0,1)
            elif train_vel == (0,1):
                train_vel = (-1,0)
            elif train_vel == (-1,0):
                train_vel = (0,-1)
            elif train_vel == (0,-1):
                train_vel = (1,0)
            # train_vel = (train_vel[1]*-1,train_vel[0]*-1) #TODO
            train_next_turn = 'S'
        elif train_next_turn == 'S':
            train_vel = train_vel
            train_next_turn = 'R'
        elif train_next_turn == 'R':
            if train_vel == (1,0):
                train_vel = (0,-1)
            elif train_vel == (0,-1):
                train_vel = (-1,0)
            elif train_vel == (-1,0):
                train_vel = (0,1)
            elif train_vel == (0,1):
                train_vel = (1,0)
            # train_vel = (train_vel[1],train_vel[0]) #TODO
            train_next_turn = 'L'

    train_coords = (x_coord, y_coord)

    return train_coords, train_vel, train_next_turn

def print_tracks(this_tracks):
    print('\n'.join([''.join(['{:}'.format(item) for item in row])
        for row in this_tracks]))

def remvove_trains(tracks):
    new_tracks = []
    for row in tracks:
        row = row.replace('>', '-')
        row = row.replace('<', '-')
        row = row.replace('^', '|')
        row = row.replace('v', '|')
        new_tracks.append(row)
    return new_tracks

def get_trains(tracks):
    trains = []
    for i in range(len(tracks)):
        for j in range(len(tracks[0])):
            this = tracks[i][j]
            if this == '^':
                # print(f'Found train at ({i},{j}), direction: N')
                trains.append([(i,j),(-1,0),'L'])
            elif this == '>':
                # print(f'Found train at ({i},{j}), direction: E')
                trains.append([(i,j),(0,1),'L'])
            elif this == 'v':
                # print(f'Found train at ({i},{j}), direction: S')
                trains.append([(i,j),(1,0),'L'])
            elif this == '<':
                # print(f'Found train at ({i},{j}), direction: W')
                trains.append([(i,j),(0,-1),'L'])
    # print(trains)
    return trains



def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
