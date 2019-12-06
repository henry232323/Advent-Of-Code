f = open("input.txt")

import math

class Graph:
    def __init__(self):
        self.edges = []
        self.nodes = []

    def add_edge(self, key1, key2, w):
        for node in self.nodes:
            if node.key == key1:
                n1 = node
            elif node.key == key2:
                n2 = node
        n1.adj.append(Edge(n2, w))
        n2.adj.append(Edge(n1, w))
        n1.adj.sort(key=lambda e: e.w)
        n2.adj.sort(key=lambda e: e.w)

    def add_node(self, key):
        self.nodes.append(Node(key))

    def find_shortest_dist(self, key1, key2):
        for node in self.nodes:
            node.visited = False
            node.dist = math.inf
            if node.key == key1:
                n1 = node
            elif node.key == key2:
                n2 = node

        n1.dist = 0
        self._traverse(n1, n2)
        return n2.dist


    def find_shortest_path(self, key1, key2):
        for node in self.nodes:
            node.parent = None
            node.visited = False
            node.dist = math.inf
            if node.key == key1:
                n1 = node
            elif node.key == key2:
                n2 = node

        n1.dist = 0
        self._traverse(n1, n2)
        return n2

    def print_shortest_path(self, key1, key2):
        node = self.find_shortest_path(key1, key2)
        self._print_path(node)
        print("DONE")

    def _print_path(self, node):
        if node.parent is not None:
            self._print_path(node.parent)
        print(node.key, end=" --> ")

    def _traverse(self, node, target):
        solved = []
        for n in self.nodes:
            n.dist = math.inf
        node.dist = 0

        while target not in solved:
            cnode = min(self.nodes, key=lambda n: (n in solved, n.dist))

            for e in cnode.adj:
                if e.n not in solved:
                    if cnode.dist + e.w < e.n.dist:
                        e.n.dist = cnode.dist + e.w
                        e.n.parent = cnode

            solved.append(cnode)


class Edge:
    def __init__(self, n, w):
        self.n = n
        self.w = w

class Node:
    def __init__(self, key):
        self.key = key
        self.adj = []
        self.dist = math.inf
        self.visited = False
        self.parent = None

    def __repr__(self):
        return f"Node(key={self.key}, dist={self.dist})"

g = Graph()
inp = f.read().split()
plans = []
for i in inp:
    a, b = i.split(")")
    if a not in plans:
        g.add_node(a)
        plans.append(a)
    if b not in plans:
        g.add_node(b)
        plans.append(b)
    g.add_edge(b, a, 1)


print(g.find_shortest_dist("YOU", "SAN") - 2)
