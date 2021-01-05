import unittest
import math
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph


class GraphAlgoTest(unittest.TestCase):

    def test_get_graph(self):
        graph = DiGraph()
        for i in range(5):
            graph.add_node(i)
        graph.add_edge(0, 1, 2.3)
        graph.add_edge(0, 3, 1.2)
        graph.add_edge(1, 2, 4.5)
        graph.add_edge(1, 4, 4.9)
        graph.add_edge(3, 2, 1.34)
        graph.add_edge(2, 1, 4.5)
        graph_algo = GraphAlgo(graph)
        self.assertEqual(graph, graph_algo.get_graph())

    def test_save_and_load(self):
        file_path = "unittest.json"
        graph = DiGraph()
        for i in range(9):
            graph.add_node(i)
        graph.add_edge(0, 1, 2.3)
        graph.add_edge(0, 3, 1.2)
        graph.add_edge(0, 2, 1.0)
        graph.add_edge(1, 4, 4.5)
        graph.add_edge(1, 3, 4.9)
        graph.add_edge(1, 7, 8.5)
        graph.add_edge(2, 5, 6.1)
        graph.add_edge(3, 2, 1.34)
        graph.add_edge(4, 3, 4.5)
        graph.add_edge(4, 2, 3.7)
        graph.add_edge(4, 5, 0.73)
        graph.add_edge(4, 6, 4.9)
        graph.add_edge(5, 2, 6.1)
        graph.add_edge(6, 5, 1.34)
        graph.add_edge(6, 7, 2.9)
        graph.add_edge(7, 6, 2.9)
        graph.add_edge(7, 1, 8.5)
        graph.add_edge(7, 8, 2.35)
        graph.add_edge(7, 4, 5.0)
        graph.add_edge(8, 7, 4.5)
        graph_algo = GraphAlgo(graph)
        graph_algo.save_to_json(file_path)
        graph_algo = GraphAlgo()
        graph_algo.load_from_json(file_path)
        self.assertEqual(graph, graph_algo.get_graph())
        graph.remove_edge(3, 2)
        self.assertNotEqual(graph, graph_algo.get_graph())

    def test_shortest_path(self):
        graph = DiGraph()
        for i in range(9):
            graph.add_node(i)
        graph.add_edge(0, 1, 2.3)
        graph.add_edge(0, 3, 1.2)
        graph.add_edge(0, 2, 1.0)
        graph.add_edge(1, 4, 4.5)
        graph.add_edge(1, 3, 4.9)
        graph.add_edge(1, 7, 8.5)
        graph.add_edge(2, 5, 6.1)
        graph.add_edge(3, 2, 1.34)
        graph.add_edge(4, 3, 4.5)
        graph.add_edge(4, 2, 3.7)
        graph.add_edge(4, 5, 0.73)
        graph.add_edge(4, 6, 4.9)
        graph.add_edge(5, 2, 6.1)
        graph.add_edge(6, 5, 1.34)
        graph.add_edge(6, 7, 2.9)
        graph.add_edge(7, 6, 2.9)
        graph.add_edge(7, 1, 8.5)
        graph.add_edge(7, 8, 2.35)
        graph.add_edge(7, 4, 5.0)
        graph.add_edge(8, 7, 4.5)
        graph.add_edge(3, 0, 9.5)
        graph.add_edge(2, 3, 5.5)
        graph_algo = GraphAlgo(graph)
        path = graph_algo.shortest_path(6, 0)
        actual = (21.9, [6, 7, 4, 3, 0])
        self.assertEqual(actual, path)
        path = graph_algo.shortest_path(6, 9)
        actual = (math.inf, [])
        self.assertEqual(actual, path)
        path = graph_algo.shortest_path(0, 1)
        actual = (2.3, [0, 1])
        self.assertEqual(actual, path)
        path = graph_algo.shortest_path(2, 8)
        actual = (28.15, [2, 3, 0, 1, 7, 8])
        self.assertEqual(actual, path)
        path = graph_algo.shortest_path(8, 2)
        actual = (15.2, [8, 7, 4, 2])
        self.assertEqual(actual, path)
        graph_algo.get_graph().remove_edge(2, 3)
        path = graph_algo.shortest_path(2, 8)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        graph_algo_2 = GraphAlgo()
        for i in range(11):
            graph_algo_2.get_graph().add_node(i)
        for i in range(10):
            graph_algo_2.get_graph().add_edge(i, i+1, i+1)

        for i in graph_algo_2.get_graph().v_size()-1:
            weight_path = graph_algo_2.shortest_path(i, i+1)[0]
            self.assertNotEqual(math.inf, weight_path)














if __name__ == "__main__":
    unittest.main()
