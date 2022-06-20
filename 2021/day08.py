import lib.commons as commons
import statistics

input_file = commons.get_input_filename()
readings = commons.read_file_to_list(input_file)


def part_one(readings):
    uniq_segments_count = 0
    for reading in readings:
        inputs = reading.split('|')[-1].strip().split()
        for input in inputs:
            if len(input) in [2, 4, 3, 7]:
                uniq_segments_count += 1
    return uniq_segments_count


def part_two(readings):
    ouput_sum = 0
    for reading in readings:
        ouput_num = ""
        known_numbers = {}
        inputs = reading.split('|')[0].strip().split()
        outputs = reading.split('|')[-1].strip().split()
        while len(known_numbers) != 10:
            #         for _ in range(10):
            for input in inputs:
                if len(input) == 2:
                    known_numbers[1] = input
                elif len(input) == 4:
                    known_numbers[4] = input
                elif len(input) == 3:
                    known_numbers[7] = input
                elif len(input) == 7:
                    known_numbers[8] = input
                # 9 = 6chars and all of 3
                elif len(input) == 6 and all(elem in sorted(input) for elem in sorted(known_numbers.get(3, 'x'))):
                    known_numbers[9] = input
                # 0 = 6chars and all of 1
                elif len(input) == 6 and all(elem in sorted(input) for elem in sorted(known_numbers.get(1, 'x'))):
                    known_numbers[0] = input
                # 6 = other 6char
                elif len(input) == 6:
                    known_numbers[6] = input
                # 3 = 5chars and all of 7
                elif len(input) == 5 and all(elem in sorted(input) for elem in sorted(known_numbers.get(7, 'x'))):
                    known_numbers[3] = input
                # 5 = 5chars and all of 6, bar 1
                elif len(input) == 5 and [elem in sorted(input) for elem in sorted(known_numbers.get(6, 'x'))].count(False) == 1:
                    known_numbers[5] = input
                else:
                    known_numbers[2] = input
        for output in outputs:
            num = [k for k, v in known_numbers.items() if sorted(v) == sorted(output)][0]
            ouput_num += str(num)
#         print(ouput_num)
        ouput_sum += int(ouput_num)
    return ouput_sum


print(part_one(readings))
print(part_two(readings))
