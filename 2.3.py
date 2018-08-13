def find_non_irrigation():
    global farm, m, n
    for i in range(0, m):
        for j in range(0, n):
            if farm[i][j] != '.':
                return i, j
    return None


def is_connected(a, b, d):
    global flag
    result = 0
    if d == 0:
        if flag[a][1] == '1' and flag[b][3] == '1':
            result = 1
    elif d == 1:
        if flag[a][3] == '1' and flag[b][1] == '1':
            result = 1
    elif d == 2:
        if flag[a][2] == '1' and flag[b][0] == '1':
            result = 1
    else:
        if flag[a][0] == '1' and flag[b][2] == '1':
            result = 1
    return result


def dfs(x, y):
    global farm, m, n, dir
    temp = farm[x][y]
    farm[x][y] = '.'
    print(x, y)
    for i in range(0, 4):
        u = x + dir[i][0]
        v = y + dir[i][1]
        if u < 0 or u >= m or v < 0 or v >= n:
            continue
        if farm[u][v] == '.':
            continue
        if is_connected(temp, farm[u][v], i):
            dfs(u, v)
        else:
            continue


if __name__ == "__main__":
    farm = []
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 按上、右、下、左方向有无水道，将11种管道编码，例如'A':1001,'B':1100……
    flag = {'A': '1001', 'B': '1100', 'C': '0011', 'D': '0110', 'E': '1010', 'F': '0101', 'G': '1101', 'H': '1011',
            'I': '0111', 'J': '1110', 'K': '1111'}
    m, n = [int(x) for x in input("Please enter the info of farm:").split(' ')]
    i = m

    while i:
        i -= 1
        farm.append(list(input("Please enter the info of each line:")))

    cnt = 0
    res = find_non_irrigation()
    while res:
        x, y = res
        dfs(x, y)
        cnt += 1
        res = find_non_irrigation()

    print(cnt)
