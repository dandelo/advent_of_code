import lib.commons as commons
import statistics

input_file = commons.get_input_filename()
positions = commons.read_file_to_list(input_file)[0].split(',')
positions = list(map(int, positions))


def part_one(positions):
    costs = []
    target = statistics.median(positions)
    cost = sum(abs(i - target) for i in positions)
    costs.append(cost)
    return int(min(costs))


def part_two(positions):
    costs = []
    for target in range(min(positions), max(positions) + 1):
        cost = 0
        for i in positions:
            distance_from_target = abs(i - target)
            this_cost = distance_from_target * (distance_from_target + 1) / 2
            cost += this_cost
        costs.append(cost)
    return int(min(costs))


print(part_one(positions))
print(part_two(positions))
