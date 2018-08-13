class ArcNode:
    def __init__(self, to, dur, no, next=None):
        self.to = to
        self.dur = dur
        self.no = no
        self.next = next

    def __str__(self):
        return '(' + str(self.to) + ',' + str(self.dur) + ',' + str(self.no) + ')'


def critical_path(n, m):
    ee = [0 for i in range(0, n)]
    el = [0 for i in range(0, n)]
    top1, top2 = -1, -1
    for i in range(0, n):
        if in_degree[i] == 0:
            in_degree[i] = top1
            top1 = i

    for i in range(0, n):
        if top1 == -1:
            print("Cycle exists!")
            return
        else:
            j = top1
            top1 = in_degree[top1]
            p = out_list[j]
            while p:
                k = p.to
                in_degree[k] -= 1
                if in_degree[k] == 0:
                    in_degree[k] = top1
                    top1 = k
                ee[k] = max(ee[j] + p.dur, ee[k])
                p = p.next

    for i in range(0, n):
        el[i] = max(ee)
        if out_degree[i] == 0:
            out_degree[i] = top2
            top2 = i

    for i in range(0, n):
        j = top2
        top2 = out_degree[top2]
        q = in_list[j]
        while q:
            k = q.to
            out_degree[k] -= 1
            if out_degree[k] == 0:
                out_degree[k] = top2
                top2 = k
            el[k] = min(el[j] - q.dur, el[k])
            q = q.next

    ae = [0 for i in range(0, m + 1)]
    al = [ee[n - 1] for i in range(0, m + 1)]
    print("Critical activities are:", end=':')
    for i in range(0, n):
        t = out_list[i]
        while t:
            j = t.to
            k = t.no
            ae[k] = ee[i]
            al[k] = el[j] - t.dur
            if ae[k] == al[k]:
                is_critical[k] = 1
                print(k, end=' ')
            t = t.next
    print()


if __name__ == '__main__':

    with open('2.14') as fp:
        n = int(fp.readline())
        out_list = [0 for i in range(0, n)]
        in_list = [0 for i in range(0, n)]
        in_degree = [0 for i in range(0, n)]
        out_degree = [0 for i in range(0, n)]
        m = int(fp.readline())
        is_critical = [0 for i in range(0, m + 1)]
        for data in fp.readlines():
            origin, to, dur, no = [int(x) for x in data.split(',')]
            out_degree[origin] += 1
            t = ArcNode(to, dur, no)
            if out_list[origin] == 0:
                out_list[origin] = t
            else:
                p = out_list[origin]
                while p.next:
                    p = p.next
                p.next = t

            in_degree[to] += 1
            s = ArcNode(origin, dur, no)
            if in_list[to] == 0:
                in_list[to] = s
            else:
                q = in_list[to]
                while q.next:
                    q = q.next
                q.next = s

    critical_path(n, m)
