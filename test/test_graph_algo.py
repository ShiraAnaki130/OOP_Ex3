import unittest
import math
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph
import random


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
        graph.add_edge(0, 1, 2.3938753352369698)
        graph.add_edge(0, 3, 1.2938753352369698)
        graph.add_edge(0, 2, 1.0938753352369698)
        graph.add_edge(1, 4, 4.5938753352369698)
        graph.add_edge(1, 3, 4.9938753352369698)
        graph.add_edge(1, 7, 8.5938753352369698)
        graph.add_edge(2, 5, 6.1938753352369698)
        graph.add_edge(3, 2, 1.3438753352369698)
        graph.add_edge(4, 3, 4.5938753352369698)
        graph.add_edge(4, 2, 3.7938753352369698)
        graph.add_edge(4, 5, 0.7338753352369698)
        graph.add_edge(4, 6, 4.9938753352369698)
        graph.add_edge(5, 2, 6.1938753352369698)
        graph.add_edge(6, 5, 1.3438753352369698)
        graph.add_edge(6, 7, 2.9938753352369698)
        graph.add_edge(7, 6, 2.9938753352369698)
        graph.add_edge(7, 1, 8.5938753352369698)
        graph.add_edge(7, 8, 2.2538753352369698)
        graph.add_edge(7, 4, 5.0938753352369698)
        graph.add_edge(8, 7, 4.5938753352369698)
        graph.add_edge(3, 0, 9.5938753352369698)
        graph.add_edge(2, 3, 5.5938753352369698)
        graph_algo = GraphAlgo(graph)
        bol = False
        path = graph_algo.shortest_path(6, 0)
        if (path[0] - 22.2755013409478792) < 0.001:
            bol = True
        actual = [6, 7, 4, 3, 0]
        self.assertTrue(bol)
        self.assertEqual(actual, path[1])

        #path = graph_algo.shortest_path(6, 9)
        #actual_dist = (math.inf, [])
        #self.assertTupleEqual(actual, path)

        bol = False
        path = graph_algo.shortest_path(0, 1)
        if (path[0] - 2.3938753352369698) < 0.001:
            bol = True
        actual = [0, 1]
        self.assertTrue(bol)
        self.assertEqual(actual, path[1])

        bol = False
        path = graph_algo.shortest_path(2, 8)
        if (path[0] - 28.429376676184849) < 0.001:
            bol = True
        actual = [2, 3, 0, 1, 7, 8]
        self.assertTrue(bol)
        self.assertEqual(actual, path[1])

        bol = False
        path = graph_algo.shortest_path(8, 2)
        if (path[0] - 13.4816260057109094) < 0.001:
            bol = True
        actual = [8, 7, 4, 2]
        self.assertTrue(bol)
        self.assertEqual(actual, path[1])

        graph_algo.get_graph().remove_edge(2, 3)
        path = graph_algo.shortest_path(2, 8)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        graph_algo_2 = GraphAlgo()
        for i in range(11):
            graph_algo_2.get_graph().add_node(i)
        for i in range(10):
            graph_algo_2.get_graph().add_edge(i, i+1, i+1)

        for i in range(10):
            weight_path = graph_algo_2.shortest_path(i, i+1)[0]
            self.assertNotEqual(math.inf, weight_path)

    def test_connected_component(self):
        #test_0:
        graph_algo = GraphAlgo()
        list = graph_algo.connected_component(8)
        list_actual = []
        self.assertEqual(list, list_actual)

        graph = DiGraph()
        for i in range(9):
            graph.add_node(i)
        graph.add_edge(0, 1, 2.3938753352369698)
        graph.add_edge(0, 3, 1.2938753352369698)
        graph.add_edge(0, 2, 1.0938753352369698)
        graph.add_edge(1, 4, 4.5938753352369698)
        graph.add_edge(1, 3, 4.9938753352369698)
        graph.add_edge(1, 7, 8.5938753352369698)
        graph.add_edge(2, 5, 6.1938753352369698)
        graph.add_edge(3, 2, 1.3438753352369698)
        graph.add_edge(4, 3, 4.5938753352369698)
        graph.add_edge(4, 2, 3.7938753352369698)
        graph.add_edge(4, 5, 0.7338753352369698)
        graph.add_edge(4, 6, 4.9938753352369698)
        graph.add_edge(5, 2, 6.1938753352369698)
        graph.add_edge(6, 5, 1.3438753352369698)
        graph.add_edge(6, 7, 2.9938753352369698)
        graph.add_edge(7, 6, 2.9938753352369698)
        graph.add_edge(7, 1, 8.5938753352369698)
        graph.add_edge(7, 8, 2.2538753352369698)
        graph.add_edge(7, 4, 5.0938753352369698)
        graph.add_edge(8, 7, 4.5938753352369698)
        graph.add_edge(3, 0, 9.5938753352369698)
        graph.add_edge(2, 3, 5.5938753352369698)
        graph_algo = GraphAlgo(graph)
        # test_1:

        list = graph_algo.connected_component(8)
        list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(list, list_actual)

        # test_2:

        graph_algo.get_graph().remove_edge(3, 2)
        list = graph_algo.connected_component(0)
        list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # list2 = graph_algo.connected_components()
        # print(list2)
        self.assertEqual(list, list_actual)

        # test_3:

        graph_algo.get_graph().remove_edge(2, 3)
        list = graph_algo.connected_component(5)
        list_actual = [2, 5]
        self.assertEqual(list, list_actual)

        # test_4:

        graph_algo.get_graph().remove_edge(2, 5)
        list = graph_algo.connected_component(5)
        list_actual = [5]
        self.assertEqual(list, list_actual)

        # test_5:

        graph_algo.get_graph().add_edge(2, 5, 6.1)
        list = graph_algo.connected_component(4)
        list_actual = [0, 1, 3, 4, 6, 7, 8]
        self.assertEqual(list, list_actual)

        # test_6:

        graph_algo.get_graph().remove_edge(7, 4)
        graph_algo.get_graph().remove_edge(7, 1)
        list = graph_algo.connected_component(7)
        list_actual = [6, 7, 8]
        self.assertEqual(list, list_actual)

        # test_7:

        graph_algo.get_graph().add_edge(2, 3, 5.5)
        graph_algo.get_graph().remove_edge(5, 2)
        list = graph_algo.connected_component(2)
        list_actual = [0, 1, 2, 3, 4]
        self.assertEqual(list, list_actual)

    def test_connected_components(self):
        # test_0 :
        graph_algo = GraphAlgo()
        list = graph_algo.connected_components()
        list_actual = []
        self.assertEqual(list, list_actual)

        graph = DiGraph()
        for i in range(9):
            graph.add_node(i)
        graph.add_edge(0, 1, 2.3938753352369698)
        graph.add_edge(0, 3, 1.2938753352369698)
        graph.add_edge(0, 2, 1.0938753352369698)
        graph.add_edge(1, 4, 4.5938753352369698)
        graph.add_edge(1, 3, 4.9938753352369698)
        graph.add_edge(1, 7, 8.5938753352369698)
        graph.add_edge(2, 5, 6.1938753352369698)
        graph.add_edge(3, 2, 1.3438753352369698)
        graph.add_edge(4, 3, 4.5938753352369698)
        graph.add_edge(4, 2, 3.7938753352369698)
        graph.add_edge(4, 5, 0.7338753352369698)
        graph.add_edge(4, 6, 4.9938753352369698)
        graph.add_edge(5, 2, 6.1938753352369698)
        graph.add_edge(6, 5, 1.3438753352369698)
        graph.add_edge(6, 7, 2.9938753352369698)
        graph.add_edge(7, 6, 2.9938753352369698)
        graph.add_edge(7, 1, 8.5938753352369698)
        graph.add_edge(7, 8, 2.2538753352369698)
        graph.add_edge(7, 4, 5.0938753352369698)
        graph.add_edge(8, 7, 4.5938753352369698)
        graph.add_edge(3, 0, 9.5938753352369698)
        graph.add_edge(2, 3, 5.5938753352369698)
        graph_algo = GraphAlgo(graph)

        #test_1:
        list = graph_algo.connected_components()
        list_actual = [[0, 1, 2, 3, 4, 5, 6, 7, 8]]
        self.assertEqual(list, list_actual)

        #test_2:
        graph_algo.get_graph().remove_edge(3, 2)
        list = graph_algo.connected_components()
        list_actual = [[0, 1, 2, 3, 4, 5, 6, 7, 8]]
        self.assertEqual(list, list_actual)

        #test_3:
        graph_algo.get_graph().remove_edge(2, 3)
        list = graph_algo.connected_components()
        list_actual = [[0, 1, 3, 4, 6, 7, 8], [2, 5]]
        self.assertEqual(list, list_actual)

        #test_4:
        graph_algo.get_graph().remove_edge(2, 5)
        list = graph_algo.connected_components()
        list_actual = [[0, 1, 3, 4, 6, 7, 8], [2], [5]]
        self.assertEqual(list, list_actual)

        #test_5:
        graph_algo.get_graph().add_edge(2, 5, 6.1)
        graph_algo.get_graph().remove_edge(7, 4)
        graph_algo.get_graph().remove_edge(7, 1)
        list = graph_algo.connected_components()
        list_actual = [[0, 1, 3, 4], [2, 5], [6, 7, 8]]
        self.assertEqual(list, list_actual)

        #test_6:
        graph_algo.get_graph().add_edge(2, 3, 5.5)
        graph_algo.get_graph().remove_edge(5, 2)
        list = graph_algo.connected_components()
        list_actual = [[0, 1, 2, 3, 4], [5], [6, 7, 8]]
        self.assertEqual(list, list_actual)

        #test_7:
        graph_algo.get_graph().add_edge(5, 2, 6.1)
        graph_algo.get_graph().remove_edge(2, 5)
        list = graph_algo.connected_components()
        list_actual = [[0, 1, 2, 3, 4, 5, 6, 7, 8]]
        self.assertEqual(list, list_actual)

    def test_create_one_hundred(self):
        graph = DiGraph()
        for i in range(100):
            x_random = random.uniform(35.18, 35.2)
            y_random = random.uniform(32.1, 32.2)
            graph.add_node(i, (x_random, y_random, 0.0))

        for i in range(100):
            weight = random.uniform(0.0, 2.0)
            graph.add_edge(i, i+1, weight)
            if i != 0:
                graph.add_edge(i, i - 1, weight)
        graph_algo = GraphAlgo(graph)

    def test_create_ten_power_four(self):
        vertexes = 10 ** 4
        graph = DiGraph()
        for i in range(vertexes):
            x_random = random.uniform(35.18, 35.2)
            y_random = random.uniform(32.1, 32.2)
            graph.add_node(i, (x_random, y_random, 0.0))

        for i in range(vertexes):
            weight = random.uniform(0.0, 2.0)
            if i != 0:
                graph.add_edge(i, i - 1, weight)
            graph.add_edge(i, i+1, weight)

        graph_algo = GraphAlgo(graph)

    def test_create_ten_power_six(self):
        vertexes = 10 ** 6
        graph = DiGraph()
        for i in range(vertexes):
            x_random = random.uniform(35.18, 35.2)
            y_random = random.uniform(32.1, 32.2)
            graph.add_node(i, (x_random, y_random, 0.0))

        for i in range(vertexes):
            weight = random.uniform(0.0, 2.0)
            if i != 0:
                graph.add_edge(i, i - 1, weight)
            graph.add_edge(i, i + 1, weight)

        # graph_algo = GraphAlgo(graph)
        # graph_algo.plot_graph()



if __name__ == "__main__":
    unittest.main()
