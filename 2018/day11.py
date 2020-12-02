#!/usr/local/bin/python3

import numpy as np

# serial_number =  18
serial_number =  5791

def main():
    fuel_cells_grid_size = 300
    fuel_cells_grid = np.zeros((fuel_cells_grid_size, fuel_cells_grid_size))


    for i in range(fuel_cells_grid_size):
        for j in range(fuel_cells_grid_size):
            fuel_cells_grid[i][j] = calc_cell_power(i+1, j+1)

    print(fuel_cells_grid[31:36, 43:48])

    p1_max_sum, p1_ans = solve(fuel_cells_grid)
    print(f'Max total power: {p1_max_sum}')
    print(f'Max coord: {p1_ans}')

    p2_max_sum = 0
    p2_ans = ()
    for i in range(fuel_cells_grid_size):
        p2_this_sum, p2_this_ans = solve(fuel_cells_grid,i)
        if p2_this_sum > p2_max_sum:
            p2_max_sum = p2_this_sum
            p2_ans = p2_this_ans

    print(f'Max total power: {p2_max_sum}')
    print(f'Max coord: {p2_ans}')


def solve(fuel_cells_grid, sel_size = 3):
    max_sum = 0
    ans = (0,0)
    for i in range(len(fuel_cells_grid) - sel_size):
        for j in range(len(fuel_cells_grid[0] - sel_size)):
            this_sum = np.sum(fuel_cells_grid[i:i+sel_size, j:j+sel_size])
            if this_sum > max_sum:
                max_sum = this_sum
                ans = (i+1,j+1)
    return [max_sum, (ans[0], ans[1], sel_size)]

def calc_cell_power(x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    return (power_level // 100 % 10) - 5

if __name__ == '__main__':
    main()
