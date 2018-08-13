from collections import namedtuple


class UFset:
    """
    Union-find class
    """

    def __init__(self, n):
        self.n = n
        self.parent = [-1 for i in range(0, n + 1)]

    def find(self, x):
        p = x
        while self.parent[p] >= 0:
            p = self.parent[p]

        while x != p:
            t = self.parent[x]
            self.parent[x] = p
            x = t
        return p

    def union(self, n, m):
        r1 = self.find(n)
        r2 = self.find(m)
        t = self.parent[r1] + self.parent[r2]
        if self.parent[r1] > self.parent[r2]:
            self.parent[r1] = r2
            self.parent[r2] = t
        else:
            self.parent[r2] = r1
            self.parent[r1] = t

    def print(self):
        for i in range(1, self.n + 1):
            print(self.parent[i], end=' ')


def Kruskal():
    mst_weight = 0
    selected_edge_num = 0
    V = set()
    E = list()
    Edge = namedtuple('Edge', ['u', 'v', 'w'])
    with open('2.15') as fp:
        for line in fp.readlines():
            u, v, w = [int(x) for x in line.split()]
            E.append(Edge(u, v, w))
            V.add(u)
            V.add(v)
    # Sort edges by weight.
    E = sorted(E, key=lambda x: x.w)
    # Use the union-find set to check weather the new edge will lead to cycle.
    c = UFset(len(V))
    for (u, v, w) in E:
        if c.find(u) != c.find(v):
            print(u, v, w)
            mst_weight += w
            c.union(u, v)
            selected_edge_num += 1
            if selected_edge_num == len(V) - 1:
                break
    print("The weight of MST is:", mst_weight)


def Boruvka():
    mst_weight = 0
    V = set()
    E = list()
    Edge = namedtuple('Edge', ['u', 'v', 'w'])
    with open('2.15') as fp:
        for line in fp.readlines():
            u, v, w = [int(x) for x in line.split()]
            E.append(Edge(u, v, w))
            V.add(u)
            V.add(v)
    # Use the union-find set to check weather the new edge will lead to cycle.
    c = UFset(len(V))

    Q = set()
    for v in V:
        Q.add(c.find(v))
    while len(Q) > 1:
        # In each loop, find the shortest edge of each set which links this set to another set.
        selected_edges = set()
        for n in Q:
            shortest_linked_edge = None
            shortest_linked_edge_length = 65536
            for edge in E:
                u, v, w = edge
                if (c.find(n) == c.find(u) and c.find(n) != c.find(v)) or (
                        c.find(n) == c.find(v) and c.find(n) != c.find(u)):
                    if w < shortest_linked_edge_length:
                        shortest_linked_edge_length = w
                        shortest_linked_edge = edge
            # Avoid selecting the same edge twice.
            if shortest_linked_edge and shortest_linked_edge not in selected_edges:
                selected_edges.add(shortest_linked_edge)
        # According to the selected edges, combine sets.
        for (u, v, w) in selected_edges:
            print(u, v, w)
            c.union(u, v)
            mst_weight += w
        Q.clear()
        for v in V:
            Q.add(c.find(v))
    print("The weight of MST is:", mst_weight)


def Prim():
    mst_weight = 0
    V = set()
    E = list()
    Edge = namedtuple('Edge', ['u', 'v', 'w'])
    with open('2.15') as fp:
        for line in fp.readlines():
            u, v, w = [int(x) for x in line.split()]
            E.append(Edge(u, v, w))
            V.add(u)
            V.add(v)

    is_used = {x: 0 for x in E}
    c = UFset(len(V))
    Q = set()
    root = V.pop()
    V.add(root)
    Q.add(root)
    while Q != V:
        selected_edge = None
        selected_edge_weight = 65536
        for edge in E:
            if is_used[edge] == 0:
                u, v, w = edge
                if (c.find(u) == root and c.find(v) != root) or (c.find(v) == root and c.find(u) != root):
                    if w < selected_edge_weight:
                        selected_edge = edge
                        selected_edge_weight = edge.w

        if selected_edge:
            u, v, w = selected_edge
            print(u, v, w)
            c.union(u, v)
            mst_weight += w
            is_used[selected_edge] = 1

        for v in V:
            if c.find(v) == root:
                Q.add(v)

    print("The weight of MST is:", mst_weight)


if __name__ == "__main__":
    Kruskal()
    Boruvka()
    Prim()
