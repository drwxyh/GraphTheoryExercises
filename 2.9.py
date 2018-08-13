from collections import deque, namedtuple
import numpy as np


def bfs():
    global n, m, data
    Node = namedtuple('Node', ['v', 'c'])
    visited = np.zeros(n, dtype=int)
    Q = deque()
    Q.append(Node(0, 0))
    while Q:
        t = Q.popleft()
        for i in range(0, m):
            k = t.c * 10 + data[i]
            if not k:
                continue
            k = k % n
            if k == 0:
                return t.v * 10 + data[i]
            if not visited[k]:
                visited[k] = 1
                Q.append(Node(t.v * 10 + data[i], k))
    return 0


if __name__ == "__main__":
    with open('2.9') as fp:
        n = int(fp.readline())
        m = int(fp.readline())
        data = sorted([int(x) for x in fp.readlines()])
    res = bfs()
    print(res)
