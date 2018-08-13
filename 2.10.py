class ArcNode:
    def __init__(self, to, nx=None):
        self.to = to
        self.next = nx


def topo_sort():
    global count, vertex_list
    res = list()
    top = -1
    has_circle = False

    for i in range(0, n):
        if count[i] == 0:
            count[i] = top
            top = i

    for i in range(0, n):
        if top == -1:
            has_circle = True
            break
        else:
            j = top
            top = count[top]
            res.append(j + 1)
            t = vertex_list[j]
            while t:
                k = t.to
                count[k] -= 1
                if count[k] == 0:
                    count[k] = top
                    top = k
                t = t.next

    if has_circle:
        print('Network has a cycle!')
    else:
        print(res)


if __name__ == "__main__":
    with open('2.10') as fp:
        n, m = [int(x) for x in fp.readline().strip('\n').split(' ')]
        data = list()
        count = [0 for i in range(0, n)]
        vertex_list = [0 for i in range(0, n)]
        for x in fp.readlines():
            data.append(tuple(int(i) - 1 for i in x.strip('\n').split(' ')))

    for d in data:
        t = ArcNode(d[1])
        count[d[1]] += 1
        if vertex_list[d[0]] == 0:
            vertex_list[d[0]] = t
        else:
            p = vertex_list[d[0]]
            while p.next:
                p = p.next
            p.next = t

    topo_sort()
