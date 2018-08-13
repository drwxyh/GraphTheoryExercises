class Vertex:
    def __init__(self, vid):
        self.id = vid
        self.connectedTo = {}  # 使用字典存储相邻节点

    def add_neighbor(self, nbr, weight):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connectedTo:' + str([x.id for x in self.connectedTo])

    def get_connections(self):
        return self.connectedTo.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertexList = dict()
        self.vertexNum = 0
        self.edgeNum = 0

    def add_vertex(self, vid):
        self.vertexNum += 1
        vertex = Vertex(vid)
        self.vertexList[vid] = vertex

    def get_vertex(self, vid):
        if vid in self.vertexList:
            return self.vertexList[vid]
        else:
            return None

    def add_edge(self, f, t, weight=0):
        self.edgeNum += 1
        if f not in self.vertexList:
            self.add_vertex(f)
        if t not in self.vertexList:
            self.add_vertex(t)
        self.vertexList[f].add_neighbor(self.vertexList[t], weight)

    def get_vertices(self):
        return self.vertexList.values()

    def __iter__(self):
        return iter(self.vertexList.values())


def generate_graph():
    g = Graph()
    n, m = [int(x) for x in input("Please enter the numbers of vertices and edges: ").split(' ')]
    g.vertexNum = n
    g.edgeNum = m

    for x in range(1, n + 1):
        g.add_vertex(x)

    while m:
        m -= 1
        data = [int(x) for x in input("Please enter the info of edge: ").split(' ')]
        if len(data) == 2:
            g.add_edge(data[0], data[1])
        else:
            g.add_edge(data[0], data[1], data[2])

    out_degree = list()
    for x in g.get_vertices():
        out_degree.append(len(x.get_connections()))

    in_degrees = dict((u, 0) for u in g.get_vertices())
    out_degrees = dict((u, 0) for u in g.get_vertices())

    for u in g.get_vertices():
        out_degrees[u] = len(u.get_connections())

    for u in g.get_vertices():
        for v in u.get_connections():
            in_degrees[v] += 1

    print(out_degrees.values())
    print(in_degrees.values())


if __name__ == "__main__":
    generate_graph()
