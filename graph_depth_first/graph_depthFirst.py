from collections import deque


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)


class Vertex:
    def __init__(self, value):
        """
        Node/vertex constructor
        """
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex


class Graph:

    def __init__(self):
        self.__adj_list = {}

    def add_node(self, value):
        """ Add the node to adj_list as key and value it will be an empty list"""
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertex not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertex, weight)
        # edge2 = Edge(start_vertex)
        self.__adj_list[start_vertex].append(edge1)
        # self.__adj_list[end_vertex].append(edge2)

    def get_nodes(self):
        return self.__adj_list.keys()

    def size(self):
        return len(self.__adj_list)

    def get_neighbors(self, ver):
        return self.__adj_list.get(ver, [])

    def breadth_first(self, start_vertex):
        result = []
        visted = set()
        q = Queue()

        q.enqueue(start_vertex)
        visted.add(start_vertex)

        while len(q):
            current_vertex = q.dequeue()

            result.append(current_vertex.value)

            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visted:
                    q.enqueue(neighbor)
                    visted.add(neighbor)

        return result

    def depth_first(self,root):
        result = []

        def _walk(root):
            result.append(root.value)
            for i in self.get_neighbors(root):
                if i.vertex.value not in result:
                    _walk(i.vertex)

        _walk(root)
        return result


if __name__ == "__main__":
    g = Graph()
    a = g.add_node('A')
    b = g.add_node('B')
    e = g.add_node('E')
    c = g.add_node('C')
    d = g.add_node('D')
    g.add_edge(a, b)
    g.add_edge(b, a)
    g.add_edge(a, e)
    g.add_edge(e, a)
    g.add_edge(a, c)
    g.add_edge(b, d)
    g.add_edge(b, e)
    g.add_edge(e, d)
    g.add_edge(e, c)

    print(g.breadth_first(b))
    print(g.depth_first(b))

