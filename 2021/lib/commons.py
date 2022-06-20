import inspect
import numpy as np


def read_file_to_list(filename):
    with open(filename) as f:
        return f.read().splitlines()


def read_file_to_np_array(filename, type=np.int32):
    with open(filename) as myfile:
        return np.array([list(line.strip()) for line in myfile]).astype(type)


def get_input_filename(extension='.txt'):
    return f"inputs/{inspect.stack()[1].filename.replace('.py', extension)}"


def line_to_list(line: str):
    lst = line.split(' ')
    return [x for x in lst if x]


def print_like_aoc(array: np.ndarray):
    print(np.rot90(np.rot90(np.rot90(np.flip(array, 0)))))
