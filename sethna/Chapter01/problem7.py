"""Chapter 1, Problem 7 of Statistical Mechanics by Sethna."""

import random

import numpy as np


class Network:
    """A simple object describing a graph.

    The graph is stored as a dictionary whose keys are nodes and whose values are a set containing
    nodes in the graph with which that particular node shares an edge.
    
    """

    def __init__(self):
        """Instantiate an empty graph."""
        self.edges = dict()

    def has_node(self, node):
        """Determines whether the graph has a particular node in it."""
        return node in self.edges
    
    def add_node(self, node):
        """Adds the given node to the graph."""
        if node not in self.edges:
            self.edges[node] = set()

    def add_edge(self, node1, node2):
        """Adds an edge between two nodes."""
        self.edges[node1].add(node2)
        self.edges[node2].add(node1)

    def get_nodes(self):
        """Returns a set of all nodes in the graph."""
        return set(self.edges.keys())
    
    def get_neighbors(self, node):
        """Returns the set of all nodes neighboring `node`."""
        return self.edges[node]


class SmallWorldNetwork(Network):
    """An object describing a small world network.

    A small world network is a connected graph where every node shares an edge with its neighbors
    out to some small distance away.  Edges are then added between random pairs of nodes in the
    graph.  These extra edges are known as "shortcut connections".

    """

    def __init__(self, L, Z, p):
        """Instantiate a `SmallWorldNetwork`.

        Args:
            L: The number of nodes in the graph.
            Z: The number of neighboring edges each node has.
            p: The probability that any particular pair of nodes has a shortcut connection.

        """
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
    """Finds the path lengths from one node to all other nodes.

    This performs a breadth-first search.

    Args:
        graph: A `Network` object.
        node: The key for a node in `graph`.

    Returns:
        A `dict` whose keys are the other nodes in `graph` and whose values are the distance between
        `node` and the node specified by the key.

    """
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


def find_all_path_lengths(graph):
    """Finds the distribution of path lengths between all pairs of nodes.

    Args:
        graph: A `Network` object.

    Returns:
        A `dict` with `(node1, node2)` tuple pairs as keys and the distance between the two nodes as
        values.

    """
    all_distances = {}
    for node in graph.get_nodes():
        distances = find_path_lengths_from_node(graph, node)
        for key in distances.keys():
            pair = tuple(sorted([node, key]))
            if pair not in all_distances:
                all_distances[pair] = distances[key]
    return all_distances


def find_average_path_length(graph):
    """Calculates the mean path length between every pair of nodes.

    Args:
        graph: A `Network` object.

    Returns:
        The mean path length between every pair of nodes.

    """
    return np.mean(list(find_all_path_lengths(graph).values()))
