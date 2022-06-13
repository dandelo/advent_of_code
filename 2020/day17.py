#!/usr/local/bin/python3

import os
import numpy as np
import itertools

def main():
    initital_state = np.arange(20).reshape(4,5)

    print(f'Part 1 answer: {solve_part1(initital_state)}')

def solve_part1(initital_state):
    # dim = len(initital_state.shape)       # number of dimensions
    # offsets = [0, -1, 1]     # offsets, 0 first so the original entry is first 
    # columns = []
    # for shift in itertools.product(offsets, repeat=dim):   # equivalent to dim nested loops over offsets
    #     columns.append(np.roll(initital_state, shift, np.arange(dim))[:2,:2].ravel())
    # neighbors = np.stack(columns, axis=-1)

    
    def neighbors(array, x, y):
        rows, cols = array.shape
        return array[max(0, x-1):min(rows, x+2), max(0, y-1):min(cols, y+2)]

    neighbors = neighbors(initital_state, 1, 1)

    # # make a 3d array with the matrix entry and its four neighbors
    # neighbor_array = np.array([initital_state,
    #                         np.roll(initital_state,+1,axis=0),
    #                         np.roll(initital_state,-1,axis=0),
    #                         np.roll(initital_state,+1,axis=1),
    #                         np.roll(initital_state,-1,axis=1),
    #                         ])
    # # if you want neighbors to include wraparounds, use above; if not, prune
    # neighbor_array_pruned = neighbor_array[:,1:-1,1:-1]
    # # reshape to a 2d array entries x neighbors
    # neighbor_list = np.reshape(neighbor_array_pruned,[5,-1]).T
    # # get uniques into a dictionary 
    # neighbors = {}
    # for num in np.unique(initital_state):
    #     neighbors[num] = np.unique(neighbor_list[np.where(neighbor_list[:,0]==num)])

    return neighbors


def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file


if __name__ == '__main__':
    main()
