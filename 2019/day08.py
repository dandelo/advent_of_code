import os

transparent = '2'
white = '1'
black = '0'

def main():
    do_small = False
    if do_small:
        width = 3
        height = 2
    else:
        width = 25
        height = 6
    input_file = get_input_filename(do_small)

    with open(input_file) as f:
        input = f.read().strip('\n')
    layers = solve(input, width, height)
    solve2(layers, width, height)

def solve(image_data, width, height):
    layers = list(chunk(image_data, width*height))
    fewest_zero_layer = -1
    fewest_zeros = 99999
    for idx, layer in enumerate(layers):
        zeros_in_layer = layer.count('0')
        if zeros_in_layer < fewest_zeros:
            fewest_zeros = zeros_in_layer
            fewest_zero_layer = idx
        # print(layer)
        # print(layer.count('0'))
    print(f'fewest zeros in layer {fewest_zero_layer} (fewest_zeros)')
    ones_by_twos = layers[fewest_zero_layer].count('1') * layers[fewest_zero_layer].count('2')
    print(ones_by_twos)
    return layers

def chunk(data, size):
    for i in range(0, len(data), size):
        yield data[i:i+size]

def solve2(layers, width, height):
    image = [transparent] * width * height
    for layer in layers:
        for idx, char in enumerate(layer):
            if image[idx] == transparent:
                image[idx] = char

    for idx, i in enumerate(image):
        print(i.replace(black, ' ').replace(white, '█'), end = "")
        if (idx + 1) % width == 0:
            print()

def get_input_filename(do_small = False):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file


if __name__ == '__main__':
    main()
