def dfs(cur_x, cur_y, cur_t):
    global escape, door_x, door_y, dir, t
    # 准时到达门产生地点
    if cur_x == door_x and cur_y == door_y and cur_t == t:
        escape = True
        return
    # 剪枝操作
    temp = (t - cur_t) - abs(cur_x - door_x) - abs(cur_y - door_y)
    if temp < 0 or temp % 2:
        return
    # 尝试移动
    for i in range(0, 4):
        # 判断移动是否越界
        if cur_x + dir[i][0] in range(0, n) and cur_y + dir[i][1] in range(0, m):
            if maze[cur_x + dir[i][0]][cur_y + dir[i][1]] != 'X':
                # 将走过的地方设置为墙
                maze[cur_x + dir[i][0]][cur_y + dir[i][1]] = 'X'
                dfs(cur_x + dir[i][0], cur_y + dir[i][1], cur_t + 1)
                if escape:
                    return
                maze[cur_x + dir[i][0]][cur_y + dir[i][1]] = '.'
    return


if __name__ == "__main__":
    maze = []
    dir = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    n, m, t = [int(x) for x in input("Please enter the info of maze:").split(' ')]
    i = n
    while i:
        i -= 1
        maze.append(list(input("Please enter the info of each line:")))

    wall = 0
    for i in range(0, n):
        for j in range(0, m):
            if maze[i][j] == 'D':
                door_x, door_y = i, j
            elif maze[i][j] == 'S':
                start_x, start_y = i, j
            elif maze[i][j] == 'X':
                wall += 1

    if n * m - wall <= t:
        print('No')

    escape = False
    maze[start_x][start_y] = 'X'
    dfs(start_x, start_y, 0)

    if escape:
        print('Yes')
    else:
        print('No')
