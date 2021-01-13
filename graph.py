class Graph:

    def __init__(self, values):
        self.values = {}
        for i in values:
            self.values[i] = []

    def add_edge_directed(self, src, dest):
        if not self.values[src]:
            raise ValueError("DNE")
        self.values[src].append(dest)

    def add_edge_undirected(self, src, dest):
        if not self.values[src]:
            raise ValueError("DNE")
        if not self.values[dest]:
            raise ValueError("connection DNE")
        self.values[src].append(dest)
        self.values[dest].append(src)

    def add_node(self, value):
        if value in self.values:
            raise ValueError("in graph")
        self.values[value] = []
