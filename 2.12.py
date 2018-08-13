class ArcNode:
    def __init__(self, to, next=None):
        self.to = to
        self.next = next


def topo_sort():
    top = 0
    has_circle = False
    for i in range(1, 10):
        if count[i] == 0:
            count[i] = top
            top = i

    for i in range(1, 10):
        if top == 0:
            has_circle = True
            break
        else:
            j = top
            top = count[j]
            p = head_list[j]
            while p:
                k = p.to
                count[k] -= 1
                if count[k] == 0:
                    count[k] = top
                    top = k
                p = p.next

    if not has_circle:
        print('THESE WINDOWS ARE CLEAN')
    else:
        print('THESE WINDOWS ARE BROKEN')


if __name__ == "__main__":
    head_list = [0 for i in range(0, 10)]
    count = [0 for i in range(0, 10)]
    restrain = [[1], [1, 2], [2, 3], [3], [1, 4], [1, 2, 4, 5], [2, 3, 5, 6], [3, 6], [4, 7], [4, 5, 7, 8],
                [5, 6, 8, 9], [6, 9], [7], [7, 8], [8, 9], [9]]
    screen = []
    with open('2.12') as fp:
        fp.readline()
        for x in fp.readlines():
            if x != 'END':
                for y in x.split():
                    screen.append(int(y))

    for i in [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]:
        for x in restrain[i]:
            if x != screen[i]:
                t = ArcNode(x)
                count[x] += 1
                if head_list[screen[i]] == 0:
                    head_list[screen[i]] = t
                else:
                    p = head_list[screen[i]]
                    while p.next:
                        p = p.next
                    p.next = t

    topo_sort()
