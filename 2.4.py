from collections import namedtuple, OrderedDict


def dfs(cnt):
    global board, n, m, square_dict, kinds
    if cnt == n * n:
        return True

    for i in range(0, m):
        item = kinds[i]
        # 此类方块已用完
        if square_dict[item] == 0:
            continue
        # 非第一列，不匹配左边方块
        if cnt > 0:
            if cnt % n and item.left != kinds[board[cnt - 1]].right:
                continue

        # 非第一行，不匹配上方方块
        if cnt > n:
            if cnt // n and item.up != kinds[board[cnt - n]].down:
                continue

        square_dict[item] -= 1
        board[cnt] = i
        if dfs(cnt + 1):
            return True
        else:
            square_dict[item] += 1

    return False


if __name__ == "__main__":
    n = int(input("Please enter the size of the big square:"))
    i = n * n
    Square = namedtuple('Square', ['up', 'right', 'down', 'left'])
    squares = list()  # 存放方块数据
    board = [0] * (n * n)  # 记录每个位置放置方块的种类
    square_dict = OrderedDict()  # 记录每种方块的数量

    while i:
        i -= 1
        data = [int(x) for x in input("Please enter the value of each square:").split(' ')]
        squares.append(Square(*data))

    for square in squares:
        if square not in square_dict:
            square_dict[square] = 1
        else:
            square_dict[square] += 1
    kinds = list()

    for item in square_dict.keys():
        kinds.append(item)

    m = len(kinds)

    if dfs(0):
        print("Possible.")
    else:
        print("Impossible.")
