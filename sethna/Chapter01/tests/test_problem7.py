import unittest

from ..problem7 import Network
from ..problem7 import SmallWorldNetwork
from ..problem7 import find_path_lengths_from_node


class TestNetwork(unittest.TestCase):

    def test_network_has_node(self):
        network = Network()
        self.assertFalse(network.has_node(1))
        network.add_node(1)
        self.assertTrue(network.has_node(1))

    def test_network_edges(self):
        network = Network()
        network.add_node(1)
        network.add_node(2)
        network.add_edge(1, 2)
        self.assertSetEqual(network.get_nodes(), set([1, 2]))
        self.assertSetEqual(network.get_neighbors(1), set([2]))
        self.assertSetEqual(network.get_neighbors(2), set([1]))


class TestSmallWorldNetwork(unittest.TestCase):

    def test_small_world_network(self):
        small_world_network = SmallWorldNetwork(L=20, Z=4, p=0.2)
        self.assertTrue(small_world_network.has_node(0))
        self.assertTrue(small_world_network.has_node(19))
        self.assertFalse(small_world_network.has_node(20))
        self.assertIn(1, small_world_network.get_neighbors(0))
        self.assertIn(18, small_world_network.get_neighbors(0))


class TestFindPathLengthsFromNode(unittest.TestCase):

    def test_find_path_lengths_from_node(self):
        network = Network()
        network.add_node(1)
        network.add_node(2)
        network.add_edge(1, 2)

        distances = find_path_lengths_from_node(network, 1)
        self.assertDictEqual(distances, {2: 1})

    def test_find_path_lengths_from_node_small_world_network(self):
        small_world_network = SmallWorldNetwork(L=20, Z=4, p=0.2)
        distances = find_path_lengths_from_node(small_world_network, 0)
        self.assertSetEqual(set(distances.keys()), set(range(1, 20))) 
