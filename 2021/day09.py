import lib.commons as commons
import numpy as np

input_file = commons.get_input_filename()
with open(input_file) as myfile:
    cave_floor = np.array([list(line.strip()) for line in myfile]).astype(np.int32)


def part_one(cave_floor):
    x_len = len(cave_floor)
    y_len = len(cave_floor[0])
    low_points = []
    for (x, y), item in np.ndenumerate(cave_floor):
        cross_section = np.concatenate((cave_floor[max(x-1, 0):min(x+2, x_len), y], cave_floor[x, max(y-1, 0):min(y+2, y_len)]))
        # cross_section includes item twice, so ensure no other level items agacent and it's the lowest
        if np.count_nonzero(cross_section == item) == 2 and min(cross_section) == item:
            low_points.append(item)
    return sum(low_points) + len(low_points)


def get_low_points(cave_floor):
    x_len = len(cave_floor)
    y_len = len(cave_floor[0])
    low_points = []
    for (x, y), item in np.ndenumerate(cave_floor):
        cross_section = np.concatenate((cave_floor[max(x-1, 0):min(x+2, x_len), y], cave_floor[x, max(y-1, 0):min(y+2, y_len)]))
        # cross_section includes item twice, so ensure no other level items agacent and it's the lowest
        if np.count_nonzero(cross_section == item) == 2 and min(cross_section) == item:
            low_points.append((x, y))
    return(low_points)


def part_two(cave_floor):
    low_points = get_low_points(cave_floor)
    low_point_sizes = []
    x_len = len(cave_floor)
    y_len = len(cave_floor[0])
    for low_point in low_points:
        low_point_size = 0
        seen = []
        stack = [low_point]
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            # look left
            x = current[0]
            y = current[1]
            while x >= 0 and cave_floor[x, y] != 9:
                x -= 1
                stack.append((x, y))
            stack.pop()  # remove final value, which would have been invalid
            # look right
            x = current[0]
            y = current[1]
            while x < x_len and cave_floor[x, y] != 9:
                x += 1
                stack.append((x, y))
            stack.pop()  # remove final value, which would have been invalid
            # look up
            x = current[0]
            y = current[1]
            while y >= 0 and cave_floor[x, y] != 9:
                y -= 1
                stack.append((x, y))
            stack.pop()  # remove final value, which would have been invalid
            # look down
            x = current[0]
            y = current[1]
            while y < y_len and cave_floor[x, y] != 9:
                y += 1
                stack.append((x, y))
            stack.pop()  # remove final value, which would have been invalid

            seen.append(current)
            low_point_size += 1
        low_point_sizes.append(low_point_size)
#         print(f"size of {low_point} is {low_point_size}")
    low_point_sizes.sort()
    return np.prod(low_point_sizes[-3:])


print(part_one(cave_floor))
print(part_two(cave_floor))
