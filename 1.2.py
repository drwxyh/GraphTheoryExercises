import numpy as np


class Lake:
    def __init__(self, id, degree):
        self.id = id
        self.degree = degree


def sort_arr(arr, start):
    temp = list()
    res = list()
    for i in range(start, len(arr)):
        temp.append(arr[i])
    temp = sorted(temp, key=lambda x: x.degree, reverse=True)
    for i in range(0, start):
        res.append(arr[i])
    for x in temp:
        res.append(x)
    return res


def is_lake_exist(lake_num, degree):
    lake_list = list()
    for i in range(0, lake_num):
        lake_list.append(Lake(i, degree[i]))
    adjacency_matrix = np.zeros((lake_num, lake_num), dtype=int)
    flag = 1
    for i in range(0, lake_num):
        lake_list = sort_arr(lake_list, i)

        u = lake_list[i].id
        d = lake_list[i].degree

        if d > lake_num - i - 1:
            flag = 0
            break

        for k in range(1, d + 1):
            v = lake_list[i + k].id
            if lake_list[i + k].degree <= 0:
                flag = 0
                break
            lake_list[i + k].degree -= 1
            adjacency_matrix[u][v] = adjacency_matrix[v][u] = 1

    if flag:
        print('Yes')
        print(adjacency_matrix)
    else:
        print('No')


if __name__ == "__main__":
    with open('1.2') as fp:
        sample_num = int(fp.readline())
        while sample_num > 0:
            lake_num = int(fp.readline())
            degree = [int(x) for x in fp.readline().split()]
            is_lake_exist(lake_num, degree)
            sample_num -= 1
