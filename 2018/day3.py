#!/usr/local/bin/python

fabric_size = 1000
fabric = [[0] * fabric_size for i in range(fabric_size)]


def solve(filename='day3.input'):
    with open(filename) as f:
        parsed_file = map(parse_file_line, f)

    map(mark_fabric, parsed_file)
    print("Count of over-lapping squares: {}".format(sum(x.count('X') for x in fabric)))
    map(check_fabric, parsed_file)


def parse_file_line(line):
    line_els = line.split()
    # Remove the '@' elemet
    del line_els[1]
    # Remove # and : chars
    line_els = [s.strip('#:') for s in line_els]
    coords = line_els[1].split(',')
    dims = line_els[2].split('x')

    line_els = [line_els[0], coords[0], coords[1], dims[0], dims[1]]
    line_els = map(int, line_els)
    return line_els


def mark_fabric(location):
    id = location[0]
    x_start = location[1]
    y_start = location[2]
    width = location[3]
    length = location[4]

    for x_pos in range(0,width):
        for y_pos in range(0,length):
            if fabric[x_start + x_pos][y_start + y_pos] == 0:
                fabric[x_start + x_pos][y_start + y_pos] = id
            else:
                fabric[x_start + x_pos][y_start + y_pos] = 'X'


def check_fabric(location):
    id = location[0]
    x_start = location[1]
    y_start = location[2]
    width = location[3]
    length = location[4]

    for x_pos in range(0,width):
        for y_pos in range(0,length):
            if fabric[x_start + x_pos][y_start + y_pos] == id:
                continue
            else:
                return
    print("ID of intact claim: {}".format(id))

def print_fabric():
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in fabric]))

solve()

# print_fabric()
