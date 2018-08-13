from collections import deque


def bfs(s):
    dist = 1
    Q = list()
    Q.append(deque())
    Q.append(deque())
    a, b = 0, 1
    if check_by[s] < cur:
        Q[b].append(s)
        check_by[s] = cur
        gap_num[s] = max(gap_num[s], dist)

    while Q[b]:
        a, b = b, a
        while Q[a]:
            cur_id = Q[a].pop()
            for i in range(0, neighbor_num[str(cur_id + 7400)]):
                next_id = neighbor_area[str(cur_id + 7400)][i]
                if check_by[next_id] < cur:
                    Q[b].append(next_id)
                    check_by[next_id] = cur
                    gap_num[next_id] = max(gap_num[next_id], dist + 1)
        dist += 1


if __name__ == "__main__":
    stations = list()  # 存储公交车路线
    neighbor_num = dict()  # 存储相邻区域数目
    neighbor_area = dict()  # 存储相邻区域编号
    cur = 0
    with open('2.8') as fp:
        nz, nr = [int(x) for x in fp.readline().strip('\n').split(' ')]
        check_by = [-1 for x in range(0, nz)]  # 记录被哪个区域开始的bfs扫描过
        gap_num = [0 for x in range(0, nz)]  # i 区域距离所有车站的最大距离
        i = nz
        while i:
            i -= 1
            data = fp.readline().strip('\n').split(' ')
            if data[0] not in neighbor_num:
                neighbor_num[data[0]] = int(data[1])
            if data[0] not in neighbor_area:
                neighbor_area[data[0]] = list()
                for j in range(2, len(data)):
                    neighbor_area[data[0]].append(int(data[j]) - 7400)

        j = nr
        while j:
            j -= 1
            data = [int(x) - 7400 for x in fp.readline().strip('\n').split(' ') if int(x) > 7000]
            for item in data:
                if item not in stations:
                    stations.append(item)

    for i in stations:
        bfs(i)
        cur += 1

    t = gap_num.index(min(gap_num))
    center = str(7400 + t)
    gap = gap_num[t]
    print('%d %s' % (gap, center))
