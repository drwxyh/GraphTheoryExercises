import numpy as np


def find_range(x, y):
    ch = graph[x][y]
    left, right, up, down = width, 0, height, 0
    for i in range(0, height):
        for j in range(0, width):
            if graph[i][j] == ch:
                up = min(i, up)
                down = max(i, down)
                left = min(j, left)
                right = max(j, right)
    return up, right, down, left


def construct_graph():
    count = 0
    relation = np.zeros((26, 26), dtype=int)
    is_visited = [0 for i in range(0, 5)]
    for i in range(0, height):
        for j in range(0, width):
            ch = graph[i][j]
            v = ord(ch) - ord('A')
            if ch != '.' and is_used[v] == 0:
                is_used[v] = 1
                count += 1

            if ch == '.' or is_visited[v] == 1:
                continue
            else:
                up, right, down, left = find_range(i, j)
                for k in range(up, down + 1):
                    if graph[k][left] != ch:
                        if relation[v][ord(graph[k][left]) - 65] == 0:
                            degree[ord(graph[k][left]) - 65] += 1
                            relation[v][ord(graph[k][left]) - 65] = 1
                    if graph[k][right] != ch:
                        if relation[v][ord(graph[k][right]) - 65] == 0:
                            degree[ord(graph[k][right]) - 65] += 1
                            relation[v][ord(graph[k][right]) - 65] = 1
                for k in range(left, right + 1):
                    if graph[up][k] != ch:
                        if relation[v][ord(graph[up][k]) - 65] == 0:
                            degree[ord(graph[up][k]) - 65] += 1
                            relation[v][ord(graph[up][k]) - 65] = 1
                    if graph[down][k] != ch:
                        if relation[v][ord(graph[down][k]) - 65] == 0:
                            degree[ord(graph[down][k]) - 65] += 1
                            relation[v][ord(graph[down][k]) - 65] = 1
                is_visited[v] = 1
    return relation, count


def topo_sort(depth, count, res):
    if depth >= count:
        print(res)
        return
    for i in range(0, 26):
        if is_used[i]:
            if degree[i] == 0:
                res += chr(i + 65)
                degree[i] = -1
                for j in range(0, 26):
                    if relation[i][j] == 1:
                        degree[j] -= 1
                topo_sort(depth + 1, count, res)
                res = res[0:-2]
                degree[i] = 0
                for j in range(0, 26):
                    if relation[i][j] == 1:
                        degree[j] += 1


if __name__ == '__main__':
    graph_list = list()
    with open('2.13') as fp:
        height = int(fp.readline())
        width = int(fp.readline())
        for line in fp.readlines():
            line_list = list(line.strip())
            graph_list.append(line_list)
    graph = np.array(graph_list)
    is_used = [0 for x in range(0, 26)]
    degree = [0 for x in range(0, 26)]
    relation, count = construct_graph()
    res = str()
    topo_sort(0, count, res)
