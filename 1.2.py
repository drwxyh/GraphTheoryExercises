import numpy as np


def sort_arr(arr, start):
    temp = list()
    res = list()
    for i in range(start, len(arr)):
        temp.append(arr[i])
    temp = sorted(temp, key=lambda x: x[1], reverse=True)
    for i in range(0, start):
        res.append(arr[i])
    for x in temp:
        res.append(x)
    return res


def is_lake_exist():
    sample_num = int(input('Please type in the number of sample:'))
    while sample_num:
        sample_num -= 1
        lake_num = int(input('Please type in the number of lakes: '))
        data = [int(x) for x in input('Please type in the degree of lake: ').split(' ')]
        lake = list()
        for i in range(0, lake_num):
            lake.append([i, data[i]])

        adjacency_matrix = np.zeros((lake_num, lake_num))
        flag = 1
        for i in range(0, lake_num):
            lake = sort_arr(lake, i)
            # 当前度数最大项的序号为 u, 度数为 d
            u = lake[i][0]
            d = lake[i][1]
            # 最大度数超过剩下顶点数
            if d > lake_num - i - 1:
                flag = 0
                break
            # 其后 d 的顶点的度数减一
            for k in range(1, d + 1):
                v = lake[i + k][0]
                if lake[i + k][1] <= 0:
                    flag = 0
                    break
                lake[i + k][1] -= 1
                adjacency_matrix[u][v] = adjacency_matrix[v][u] = 1

        if flag:
            print('Yes')
            print(adjacency_matrix)
        else:
            print('No')


if __name__ == "__main__":
    is_lake_exist()
