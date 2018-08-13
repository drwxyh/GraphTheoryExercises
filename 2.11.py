class ArcNode:
    def __init__(self, to, next=None):
        self.to = to
        self.next = next


def topo_sort(c):
    res = ''
    has_circle = False
    step = 0
    top = -1
    for i in range(0, n):
        if count[i] == 0:
            count[i] = top
            top = i

    for i in range(0, c):
        step = i + 1
        if top == -1:
            has_circle = True
            break
        else:
            j = top
            res += chr(j + 65)
            top = count[j]
            p = char[j]
            while p:
                k = p.to
                count[k] -= 1
                if count[k] == 0:
                    count[k] = top
                    top = k
                p = p.next

    if not has_circle and len(res) == n:
        print('Sorted sequence determined after %d relations: %s.' % (step, res))
    else:
        if has_circle:
            print('Inconsistency found after %d relations.' % step)
        else:
            print('Sorted sequence cannot be determined.')


if __name__ == "__main__":
    with open('2.11') as fp:
        n, m = [int(x) for x in fp.readline().strip('\n').split(' ')]
        char = [0 for i in range(0, n)]
        count = [0 for i in range(0, n)]
        c = 0
        for line in fp.readlines():
            u, v = line.strip('\n').split('<')
            c += 1
            x = ord(u) - 65
            y = ord(v) - 65
            t = ArcNode(y)
            count[y] += 1
            if char[x] == 0:
                char[x] = t
            else:
                p = char[x]
                while p.next:
                    p = p.next
                p.next = t

    topo_sort(c)
