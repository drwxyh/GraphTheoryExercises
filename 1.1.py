import numpy as np


def calculate_in_out():
    data = input('Please type in the number of vertex and edge， separated by space: ').split(' ')
    n = int(data[0])
    m = int(data[1])
    adjacency_matrix = np.zeros((n, n))

    i = m
    while i:
        i -= 1
        data = input('Please type in the info of edge: ').split(' ')
        adjacency_matrix[int(data[0]) - 1][int(data[1]) - 1] = 1

    in_degree = list()
    out_degree = list()
    for i in range(0, n):
        cnt_in = 0
        cnt_out = 0
        for j in range(0, n):
            cnt_in += adjacency_matrix[j][i]
            cnt_out += adjacency_matrix[i][j]
        in_degree.append(cnt_in)
        out_degree.append(cnt_out)

    print(out_degree)
    print(in_degree)


if __name__ == "__main__":
    calculate_in_out()
