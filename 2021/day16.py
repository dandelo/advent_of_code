import lib.commons as commons
from io import StringIO
from math import prod

input_file = commons.get_input_filename()
# Read as binary, drop first chars indicating it's biary
data = bin(int(open(input_file).read().strip(), 16))[2:]
ans1 = 0


def solve(buffer):
    global ans1

    version = int(buffer.read(3), 2)
    type_id = int(buffer.read(3), 2)
    ans1 += version

    if type_id == 4:
        bit_groups = ""
        contine_reading_groups = True
        while contine_reading_groups:
            # stop reading when first bit == 0
            contine_reading_groups = bool(int(buffer.read(1)))
            bit_groups += buffer.read(4)
        return int(bit_groups, 2)

    packets_values = []
    length_type_id = buffer.read(1)
    # length-based sub-packets
    if length_type_id == "0":
        length = int(buffer.read(15), 2)
        target_length = buffer.tell() + length
        while buffer.tell() != target_length:
            packets_values.append(solve(buffer))
    # count-based sub-packets
    elif length_type_id == "1":
        num_packets = int(buffer.read(11), 2)
        for _ in range(num_packets):
            packets_values.append(solve(buffer))
    else:
        raise Exception(f'unknown length type id {length_type_id}')

    if type_id == 0:
        return sum(packets_values)
    if type_id == 1:
        return prod(packets_values)
    if type_id == 2:
        return min(packets_values)
    if type_id == 3:
        return max(packets_values)
    if type_id == 5:
        return int(packets_values[0] > packets_values[1])
    if type_id == 6:
        return int(packets_values[0] < packets_values[1])
    if type_id == 7:
        return int(packets_values[0] == packets_values[1])


packet_value = solve(StringIO(data))

print(ans1)
print(packet_value)
