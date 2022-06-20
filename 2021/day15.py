import lib.commons as commons
import networkx as nx
import numpy as np

input_file = commons.get_input_filename()
cavern = commons.read_file_to_np_array(input_file)


def solve(cavern):
    G = nx.DiGraph()
    x_len = len(cavern) - 1
    y_len = len(cavern[0]) - 1
    for (x, y), item in np.ndenumerate(cavern):
        G.add_node((x, y), pos=(x, y))

    for (x, y), item in np.ndenumerate(cavern):
        left = (max(x-1, 0), y)
        right = (min(x+1, x_len), y)
        up = (x, max(y-1, 0))
        down = (x, min(y+1, y_len))
        G.add_edge((x, y), left, weight=cavern[left])
        G.add_edge((x, y), right, weight=cavern[right])
        G.add_edge((x, y), up, weight=cavern[up])
        G.add_edge((x, y), down, weight=cavern[down])

    path = nx.dijkstra_path(G, (0, 0), (x_len, y_len), weight='weight')
    return nx.path_weight(G, path, weight="weight")


def get_five_squared_cavern(cavern):
    cavern = commons.read_file_to_np_array(input_file)
    row_one = np.append(cavern, cavern + 1, axis=1)
    row_one = np.append(row_one, cavern + 2, axis=1)
    row_one = np.append(row_one, cavern + 3, axis=1)
    row_one = np.append(row_one, cavern + 4, axis=1)

    cavern_big = np.append(row_one, row_one + 1, axis=0)
    cavern_big = np.append(cavern_big, row_one + 2, axis=0)
    cavern_big = np.append(cavern_big, row_one + 3, axis=0)
    cavern_big = np.append(cavern_big, row_one + 4, axis=0)
    cavern_big[cavern_big == 10] = 1
    cavern_big[cavern_big == 11] = 2
    cavern_big[cavern_big == 12] = 3
    cavern_big[cavern_big == 13] = 4
    cavern_big[cavern_big == 14] = 5
    cavern_big[cavern_big == 15] = 6
    cavern_big[cavern_big == 16] = 7
    cavern_big[cavern_big == 17] = 8
    return cavern_big


print(solve(cavern))
cavern_big = get_five_squared_cavern(cavern)
print(solve(cavern_big))
