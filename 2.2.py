def find_oil():
    global field, m, n
    for i in range(0, m):
        for j in range(0, n):
            if field[i][j] == 'O':
                return i, j
    return None


def dfs(x, y):
    global field, m, n, dir
    field[x][y] = 'X'
    for i in range(0, 8):
        u = x + dir[i][0]
        v = y + dir[i][1]
        if u < 0 or u >= m or v < 0 or v >= n:
            continue
        if field[u][v] == 'O':
            dfs(u, v)


if __name__ == "__main__":
    field = []
    m, n = [int(x) for x in input("Please enter the info of field(m n):").split(' ')]
    i = m
    while i:
        i -= 1
        field.append(list(input("Please enter the info of each line:")))
    dir = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    cnt = 0
    res = find_oil()
    while res:
        x, y = res
        cnt += 1
        dfs(x, y)
        res = find_oil()

    print(cnt)
