def dfs(x, y):
    global ground, dir, width, height, cnt
    cnt += 1
    ground[x][y] = 'M'
    for i in range(0, 4):
        u = x + dir[i][0]
        v = y + dir[i][1]
        if u in range(0, width) and v in range(0, height):
            # 当且仅当移动到的格子为黑格时，继续搜索
            if ground[u][v] == 'B':
                dfs(u, v)


if __name__ == "__main__":
    ground = list()
    dir = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    cnt = 0
    print("Please enter the width and height:")
    height, width = [int(x) for x in input().split(' ')]
    i = width
    print("Please enter the info of each line(Red:R,Black:B,Man:M):")
    while i:
        i -= 1
        ground.append(list(input()))

    for i in range(0, width):
        for j in range(0, height):
            if ground[i][j] == 'M':
                u, v = i, j

    dfs(u, v)
    print(cnt)
