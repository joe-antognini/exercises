"""Chapter 1, Problem 7 of Statistical Mechanics by Sethna."""

import random


class Network:

    def __init__(self):
        self.edges = dict()

    def has_node(self, node):
        return node in self.edges
    
    def add_node(self, node):
        if node not in self.edges:
            self.edges[node] = set()

    def add_edge(self, node1, node2):
        self.edges[node1].add(node2)
        self.edges[node2].add(node1)

    def get_nodes(self):
        return set(self.edges.keys())
    
    def get_neighbors(self, node):
        return self.edges[node]


class SmallWorldNetwork(Network):

    def __init__(self, L, Z, p):
        super().__init__()

        # Add the nodes to the graph.
        for i in range(L):
            self.add_node(i)

        # Add the neighboring edges.
        for i in range(L):
            for j in range(-Z // 2, Z // 2):
                if j == 0:
                    continue
                self.add_edge(i, (i - j) % L) 

        # Add the shortcuts.
        n_shortcuts = int(p * L * Z / 2)
        for _ in range(n_shortcuts):
            node1 = random.choice(list(self.get_nodes()))
            remaining_nodes = self.get_nodes() - set([node1])
            node2 = random.choice(list(remaining_nodes))
            self.add_edge(node1, node2)


def find_path_lengths_from_node(graph, node):
    distances = {node: 0}
    shell = set([node])

    while set(distances.keys()) != graph.get_nodes():
        next_shell = set()
        for n in shell:
            for neighbor in graph.get_neighbors(n):
                if neighbor not in distances:
                    distances[neighbor] = distances[n] + 1
                    next_shell.add(neighbor)
        shell = next_shell

    # Don't include the trivial zero-length path of a node to itself.
    del distances[node]
    return distances
