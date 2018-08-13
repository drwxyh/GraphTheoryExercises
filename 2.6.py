from collections import deque, namedtuple
import numpy as np
import sys


def bfs(p):
    global q, cell, directions, min_time, a_y, a_y
    # 加入队列
    q.append(p)
    while q:
        hd = q.pop()
        for i in range(0, 4):
            u = hd.x + directions[i][0]
            v = hd.y + directions[i][1]
            if u in range(0, n) and v in range(0, m) and cell[u][v] != '#':
                if cell[u][v] == 'x':
                    t = Point(u, v, hd.step + 1, hd.time + 2)
                else:
                    t = Point(u, v, hd.step + 1, hd.time + 1)
                if t.time < min_time[u][v]:
                    q.append(t)
                    min_time[u][v] = t.time
    return min_time[a_x][a_y]


if __name__ == "__main__":
    cell = []
    Point = namedtuple('Point', ['x', 'y', 'step', 'time'])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    with open('2.8') as fp:
        n, m = [int(x) for x in fp.readline().split(' ')]
        i = n
        while i:
            i -= 1
            cell.append(list(fp.readline().strip('\n')))

    q = deque()
    min_time = np.zeros((n, m), dtype=int)  # 存储从救援人位置到达i,j的最短时间
    for i in range(0, n):
        for j in range(0, m):
            min_time[i][j] = sys.maxsize
            if cell[i][j] == 'a':
                a_x, a_y = i, j
            if cell[i][j] == 'r':
                r_x, r_y = i, j
    s = Point(r_x, r_y, 0, 0)
    min_time[r_x][r_y] = 0
    res = bfs(s)

    if res == sys.maxsize:
        print("Poor angel has to stay in the cell all his life.")
    else:
        print("The least time cost: %d" % res)
