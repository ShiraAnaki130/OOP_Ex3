import math
import unittest

from src.GraphAlgo import GraphAlgo
import networkx as nx


class TestComparePython(unittest.TestCase):

    # def test_json_a0(self):
    #     graph_algo = GraphAlgo()
    #     list = graph_algo.connected_component(8)
    #     list_actual = []
    #     self.assertEqual(list, list_actual)
    #
    #     path = graph_algo.shortest_path(0, 1)
    #     actual = (math.inf, [])
    #     self.assertEqual(actual, path)
    #
    #     list = graph_algo.connected_components()
    #     list_actual = []
    #     self.assertEqual(list, list_actual)
    #
    #     graph = graph_algo.get_graph()
    #     file_path = "../data/A0"
    #     graph_algo.load_from_json(file_path)
    #     self.assertNotEqual(graph, graph_algo.get_graph())
    #
    #     list = graph_algo.connected_component(12)
    #     list_actual = []
    #     self.assertEqual(list, list_actual)
    #
    #     list = graph_algo.connected_component(10)
    #     list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #     self.assertEqual(list, list_actual)
    #
    #     path = graph_algo.shortest_path(0, 15)
    #     actual = (math.inf, [])
    #     self.assertEqual(actual, path)
    #
    #     bol = False
    #     path = graph_algo.shortest_path(10, 5)
    #     if (path[0] - 6.8766368930805189) < 0.001:
    #         bol = True
    #     actual = [10, 9, 8, 7, 6, 5]
    #     self.assertTrue(bol)
    #     self.assertEqual(actual, path[1])
    #
    #     list = graph_algo.connected_components()
    #     list_actual = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    #     self.assertEqual(list, list_actual)
    #
    #     graph_algo.get_graph().remove_edge(10, 9)
    #     graph_algo.get_graph().remove_edge(10, 0)
    #     list = graph_algo.connected_components()
    #     list_actual = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10]]
    #     self.assertEqual(list, list_actual)
    #
    #     graph_algo.get_graph().remove_edge(5, 6)
    #     list = graph_algo.connected_components()
    #     list_actual = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9], [10]]
    #     self.assertEqual(list, list_actual)
    #
    #     graph_algo.get_graph().add_edge(10, 9, 1.0887225789883779)
    #     list = graph_algo.connected_components()
    #     list_actual = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    #     self.assertEqual(list, list_actual)
    #
    # def test_json_a1(self):
    #     graph_algo = GraphAlgo()
    #     list = graph_algo.connected_component(8)
    #     list_actual = []
    #     self.assertEqual(list, list_actual)
    #
    #     path = graph_algo.shortest_path(0, 1)
    #     actual = (math.inf, [])
    #     self.assertEqual(actual, path)
    #
    #     list = graph_algo.connected_components()
    #     list_actual = []
    #     self.assertEqual(list, list_actual)
    #
    #     graph = graph_algo.get_graph()
    #     file_path = "../data/A1"
    #     graph_algo.load_from_json(file_path)
    #     self.assertNotEqual(graph, graph_algo.get_graph())
    #
    #     path = graph_algo.shortest_path(0, 20)
    #     actual = (math.inf, [])
    #     self.assertEqual(actual, path)
    #
    #     bol = False
    #     path = graph_algo.shortest_path(12, 2)
    #     if (path[0] - 10.0264751371955685) < 0.001:
    #         bol = True
    #     actual = [12, 13, 14, 15, 16, 0, 1, 2]
    #     self.assertTrue(bol)
    #     self.assertEqual(actual, path[1])
    #
    #     bol = False
    #     path = graph_algo.shortest_path(7, 3)
    #     if (path[0] - 4.4891734272772504) < 0.001:
    #         bol = True
    #     actual = [7, 6, 2, 3]
    #     self.assertTrue(bol)
    #     self.assertEqual(actual, path[1])
    #
    #     list = graph_algo.connected_component(20)
    #     list_actual = []
    #     self.assertEqual(list, list_actual)
    #     list = graph_algo.connected_components()
    #     list_actual = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
    #     self.assertEqual(list, list_actual)
    #
    #     list = graph_algo.connected_component(5)
    #     list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    #     self.assertEqual(list, list_actual)
    #
    #     graph_algo.get_graph().remove_edge(2, 1)
    #     graph_algo.get_graph().remove_edge(6, 7)
    #     list = graph_algo.connected_component(0)
    #     list_actual = [0, 1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    #     self.assertEqual(list, list_actual)
    #
    #     list = graph_algo.connected_component(2)
    #     list_actual = [2, 3, 4, 5, 6]
    #     self.assertEqual(list, list_actual)
    #
    #     list = graph_algo.connected_components()
    #     list_actual = [[0, 1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [2, 3, 4, 5, 6]]
    #     self.assertEqual(list, list_actual)
    #
    #     graph_algo.get_graph().remove_edge(2, 3)
    #     graph_algo.get_graph().remove_edge(2, 6)
    #     list = graph_algo.connected_component(2)
    #     list_actual = [2]
    #     self.assertEqual(list, list_actual)
    #
    #     list = graph_algo.connected_component(6)
    #     list_actual = [3, 4, 5, 6]
    #     self.assertEqual(list, list_actual)
    #
    #     list = graph_algo.connected_components()
    #     list_actual = [[0, 1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [2], [3, 4, 5, 6]]
    #     self.assertEqual(list, list_actual)

    def test_json_a2(self):
        graph_algo = GraphAlgo()
        # list = graph_algo.connected_component(8)
        # list_actual = []
        # self.assertEqual(list, list_actual)
        #
        # path = graph_algo.shortest_path(0, 1)
        # actual = (math.inf, [])
        # self.assertEqual(actual, path)
        #
        # list = graph_algo.connected_components()
        # list_actual = []
        # self.assertEqual(list, list_actual)

        graph = graph_algo.get_graph()
        file_path = "../data/A2"
        graph_algo.load_from_json(file_path)
        self.assertNotEqual(graph, graph_algo.get_graph())
        G = nx.Graph()
        for i in graph_algo.get_graph().get_all_v().keys():
            for j, w in graph_algo.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight = w)

        # path = graph_algo.shortest_path(0, 31)
        # actual = (math.inf, [])
        # self.assertEqual(actual, path)
        #
        # bol = False
        # path = graph_algo.shortest_path(20, 18)
        # if (path[0] - 1.4193627816078853) < 0.001:
        #     bol = True
        # actual = [20, 18]
        # self.assertTrue(bol)
        # self.assertEqual(actual, path[1])
        #
        # bol = False
        # path = graph_algo.shortest_path(16, 18)
        # if (path[0] - 5.0261273817424829) < 0.001:
        #     bol = True
        # actual = [16, 15, 14, 17, 18]
        # self.assertTrue(bol)
        # self.assertEqual(actual, path[1])
        #
        # bol = False
        # path = graph_algo.shortest_path(1, 7)
        # if (path[0] - 3.562461398997425) < 0.001:
        #     bol = True
        # actual = [1, 26, 8, 7]
        # self.assertTrue(bol)
        # self.assertEqual(actual, path[1])
        # path = nx.dijkstra_path(G, 1, 7)
        # self.assertEqual(actual, path)

        #maybe different answer
        bol = False
        path = graph_algo.shortest_path(3, 30)
        # if (path[0] - 11.8733156438490402) < 0.001:
        #     bol = True
        # actual = [3, 2, 1, 26, 8, 9, 10, 11, 20, 30]
        # self.assertTrue(bol)
        path_ = nx.dijkstra_path(G, 3, 30)
        self.assertEqual(path_, path[1])

        # self.assertEqual(actual, path)

    #     list = graph_algo.connected_component(31)
    #     list_actual = []
    #     self.assertEqual(list, list_actual)
    #     list = graph_algo.connected_components()
    #     list_actual = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]
    #     self.assertEqual(list, list_actual)
    #
    #     list = graph_algo.connected_component(6)
    #     list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    #     self.assertEqual(list, list_actual)
    #
    #     graph_algo.get_graph().remove_edge(1, 0)
    #     graph_algo.get_graph().remove_edge(8, 9)
    #     graph_algo.get_graph().remove_edge(26, 25)
    #     list = graph_algo.connected_component(1)
    #     list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    #     self.assertEqual(list, list_actual)
    #
    #     list = graph_algo.connected_components()
    #     list_actual = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]
    #     self.assertEqual(list, list_actual)
    #
    #     graph_algo.get_graph().remove_edge(8, 25)
    #     list = graph_algo.connected_components()
    #     list_actual = [[1, 2, 3, 4, 5, 6, 7, 8, 26, 27, 28, 29], [0, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 30]]
    #     self.assertEqual(list, list_actual)
    #
    #     list = graph_algo.connected_component(27)
    #     list_actual = [1, 2, 3, 4, 5, 6, 7, 8, 26, 27, 28, 29]
    #     self.assertEqual(list, list_actual)
    #
    #     list = graph_algo.connected_component(1)
    #     list_actual = [1, 2, 3, 4, 5, 6, 7, 8, 26, 27, 28, 29]
    #     self.assertEqual(list, list_actual)
    #
    # def test_json_a3(self):
    #     graph_algo = GraphAlgo()
    #     list = graph_algo.connected_component(8)
    #     list_actual = []
    #     self.assertEqual(list, list_actual)
    #
    #     path = graph_algo.shortest_path(0, 1)
    #     actual = (math.inf, [])
    #     self.assertEqual(actual, path)
    #
    #     list = graph_algo.connected_components()
    #     list_actual = []
    #     self.assertEqual(list, list_actual)
    #
    #     graph = graph_algo.get_graph()
    #     file_path = "../data/A3"
    #     graph_algo.load_from_json(file_path)
    #     self.assertNotEqual(graph, graph_algo.get_graph())







if __name__ == '__main__':
    unittest.main()