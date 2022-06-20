import lib.commons as commons

input_file = commons.get_input_filename()
lines = commons.read_file_to_list(input_file)


def solve(fishies, num_days=80):
    reset_timer = 6
    new_fish_timer = 8
    for _ in range(num_days):
        fishies = {k-1: v for k, v in fishies.items()}
        spawning_fishes_count = fishies.pop(-1, 0)
        fishies[reset_timer] = fishies.get(reset_timer, 0) + spawning_fishes_count
        fishies[new_fish_timer] = spawning_fishes_count
    return sum(fishies.values())


fishies = list(map(int, lines[0].split(',')))
fishies_dict = {}
for i in fishies:
    fishies_dict[i] = fishies_dict.get(i, 0) + 1

print(solve(fishies_dict, 80))
print(solve(fishies_dict, 256))
