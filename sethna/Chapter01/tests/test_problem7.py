import unittest

from ..problem7 import Network
from ..problem7 import SmallWorldNetwork
from ..problem7 import find_all_path_lengths
from ..problem7 import find_average_path_length
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

        small_world_network = SmallWorldNetwork(L=6, Z=1, p=0)
        distances = find_path_lengths_from_node(small_world_network, 0)
        self.assertEqual(max(distances.values()), 3)


class TestFindAllPathLengths(unittest.TestCase):

    def test_find_all_path_lengths(self):
        graph = SmallWorldNetwork(L=20, Z=2, p=0)
        all_distances = find_all_path_lengths(graph)
        expected_keys = set((i, j) for i in range(20) for j in range(i+1, 20))
        self.assertSetEqual(set(all_distances.keys()), expected_keys)


class TestFindAveragePathLength(unittest.TestCase):

    def test_find_average_path_length(self):
        graph = SmallWorldNetwork(L=20, Z=2, p=0.2)
        average_path_length = find_average_path_length(graph)
        self.assertGreater(average_path_length, 0)
        self.assertLess(average_path_length, 10)
