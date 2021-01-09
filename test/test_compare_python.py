import math
import unittest


from src.GraphAlgo import GraphAlgo
import networkx as nx


class TestComparePython(unittest.TestCase):

    def test_json_a0(self):
        graph_algo = GraphAlgo()
        list = graph_algo.connected_component(8)
        list_actual = []
        self.assertEqual(list, list_actual)

        path = graph_algo.shortest_path(0, 1)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        list = graph_algo.connected_components()
        list_actual = []
        self.assertEqual(list, list_actual)

        graph = graph_algo.get_graph()
        file_path = "../data/A0"
        graph_algo.load_from_json(file_path)
        self.assertNotEqual(graph, graph_algo.get_graph())
        G = nx.DiGraph()
        for i in graph_algo.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph_algo.get_graph().get_all_v().keys():
            for j, w in graph_algo.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)

        list = graph_algo.connected_component(12)
        list_actual = []
        self.assertEqual(list, list_actual)

        list = graph_algo.connected_component(10)
        list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(list, list_actual)

        path = graph_algo.shortest_path(0, 15)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        path = graph_algo.shortest_path(10, 5)
        actual_path = nx.dijkstra_path(G, 10, 5)
        actual_dist = nx.dijkstra_path_length(G, 10, 5)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        list_actual = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        self.assertEqual(list, list_actual)

        graph_algo.get_graph().remove_edge(10, 9)
        G.remove_edge(10, 9)
        G.remove_edge(10, 0)
        graph_algo.get_graph().remove_edge(10, 0)
        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        list_actual = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        list_actual = [list_actual[1], list_actual[0]]
        self.assertEqual(list, list_actual)
        #pass
        graph_algo.get_graph().remove_edge(5, 6)
        G.remove_edge(5, 6)
        # list = graph_algo.connected_components()
        # nx_components = nx.strongly_connected_components(G)
        # temp = []
        # list_actual = []
        # for n in nx_components:
        #     for i in n:
        #         temp.append(i)
        #     list_actual.append(temp)
        #     temp = []
        # list_actual = [list_actual[1], list_actual[2], list_actual[0]]
        # self.assertEqual(list, list_actual)

        graph_algo.get_graph().add_edge(10, 9, 1.0887225789883779)
        G.add_edge(10, 9)
        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        list_actual = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        self.assertEqual(list, list_actual)

    def test_json_a1(self):
        graph_algo = GraphAlgo()
        list = graph_algo.connected_component(8)
        list_actual = []
        self.assertEqual(list, list_actual)

        path = graph_algo.shortest_path(0, 1)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        list = graph_algo.connected_components()
        list_actual = []
        self.assertEqual(list, list_actual)

        graph = graph_algo.get_graph()
        file_path = "../data/A1"
        graph_algo.load_from_json(file_path)
        self.assertNotEqual(graph, graph_algo.get_graph())
        G = nx.DiGraph()
        for i in graph_algo.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph_algo.get_graph().get_all_v().keys():
            for j, w in graph_algo.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)

        path = graph_algo.shortest_path(0, 20)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        path = graph_algo.shortest_path(12, 2)
        actual_path = nx.dijkstra_path(G, 12, 2)
        actual_dist = nx.dijkstra_path_length(G, 12, 2)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        path = graph_algo.shortest_path(7, 3)
        actual_path = nx.dijkstra_path(G, 7, 3)
        actual_dist = nx.dijkstra_path_length(G, 7, 3)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        list = graph_algo.connected_component(20)
        list_actual = []
        self.assertEqual(list, list_actual)
        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        list_actual = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        self.assertEqual(list, list_actual)

        list = graph_algo.connected_component(5)
        list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(list, list_actual)

        graph_algo.get_graph().remove_edge(2, 1)
        graph_algo.get_graph().remove_edge(6, 7)
        G.remove_edge(2, 1)
        G.remove_edge(6, 7)
        list = graph_algo.connected_component(0)
        list_actual = [0, 1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(list, list_actual)

        list = graph_algo.connected_component(2)
        list_actual = [2, 3, 4, 5, 6]
        self.assertEqual(list, list_actual)

        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        list_actual = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        list_actual = [list_actual[1], list_actual[0]]
        self.assertEqual(list, list_actual)

        graph_algo.get_graph().remove_edge(2, 3)
        graph_algo.get_graph().remove_edge(2, 6)
        G.remove_edge(2, 3)
        G.remove_edge(2, 6)
        list = graph_algo.connected_component(2)
        list_actual = [2]
        self.assertEqual(list, list_actual)

        list = graph_algo.connected_component(6)
        list_actual = [3, 4, 5, 6]
        self.assertEqual(list, list_actual)

        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        list_actual = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        list_actual = [list_actual[2], list_actual[0], list_actual[1]]
        self.assertEqual(list, list_actual)

    def test_json_a2(self):
        graph_algo = GraphAlgo()
        list = graph_algo.connected_component(8)
        list_actual = []
        self.assertEqual(list, list_actual)

        path = graph_algo.shortest_path(0, 1)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        list = graph_algo.connected_components()
        list_actual = []
        self.assertEqual(list, list_actual)

        graph = graph_algo.get_graph()
        file_path = "../data/A2"
        graph_algo.load_from_json(file_path)
        self.assertNotEqual(graph, graph_algo.get_graph())
        G = nx.DiGraph()
        for i in graph_algo.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph_algo.get_graph().get_all_v().keys():
            for j, w in graph_algo.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight = w)

        path = graph_algo.shortest_path(0, 31)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        path = graph_algo.shortest_path(20, 18)
        actual_path = nx.dijkstra_path(G, 20, 18)
        actual_dist = nx.dijkstra_path_length(G, 20, 18)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        path = graph_algo.shortest_path(16, 18)
        actual_path = nx.dijkstra_path(G, 16, 18)
        actual_dist = nx.dijkstra_path_length(G, 16, 18)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        path = graph_algo.shortest_path(1, 7)
        actual_path = nx.dijkstra_path(G, 1, 7)
        actual_dist = nx.dijkstra_path_length(G, 1, 7)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        path = graph_algo.shortest_path(3, 30)
        actual_path = nx.dijkstra_path(G, 3, 30)
        actual_dist = nx.dijkstra_path_length(G, 3, 30)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        list = graph_algo.connected_component(31)
        list_actual = []
        self.assertEqual(list, list_actual)
        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        self.assertEqual(list, list_actual)

        list = graph_algo.connected_component(6)
        list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        self.assertEqual(list, list_actual)

        graph_algo.get_graph().remove_edge(1, 0)
        graph_algo.get_graph().remove_edge(8, 9)
        graph_algo.get_graph().remove_edge(26, 25)
        G.remove_edge(1, 0)
        G.remove_edge(8, 9)
        G.remove_edge(26, 25)
        list = graph_algo.connected_component(1)
        list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        self.assertEqual(list, list_actual)

        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        list_actual = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        self.assertEqual(list, list_actual)

        graph_algo.get_graph().remove_edge(8, 25)
        G.remove_edge(8, 25)
        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        list_actual = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        list_actual = [list_actual[1], list_actual[0]]
        self.assertEqual(list, list_actual)

        list = graph_algo.connected_component(27)
        list_actual = [1, 2, 3, 4, 5, 6, 7, 8, 26, 27, 28, 29]
        self.assertEqual(list, list_actual)

        list = graph_algo.connected_component(1)
        list_actual = [1, 2, 3, 4, 5, 6, 7, 8, 26, 27, 28, 29]
        self.assertEqual(list, list_actual)

    def test_json_a3(self):
        graph_algo = GraphAlgo()
        list = graph_algo.connected_component(8)
        list_actual = []
        self.assertEqual(list, list_actual)

        path = graph_algo.shortest_path(0, 1)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        list = graph_algo.connected_components()
        list_actual = []
        self.assertEqual(list, list_actual)

        graph = graph_algo.get_graph()
        file_path = "../data/A3"
        graph_algo.load_from_json(file_path)
        self.assertNotEqual(graph, graph_algo.get_graph())
        G = nx.DiGraph()
        for i in graph_algo.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph_algo.get_graph().get_all_v().keys():
            for j, w in graph_algo.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)

        path = graph_algo.shortest_path(0, 49)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        path = graph_algo.shortest_path(90, 2)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        path = graph_algo.shortest_path(3, 13)
        actual_path = nx.dijkstra_path(G, 3, 13)
        actual_dist = nx.dijkstra_path_length(G, 3, 13)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        path = graph_algo.shortest_path(4, 40)
        actual_path = nx.dijkstra_path(G, 4, 40)
        actual_dist = nx.dijkstra_path_length(G, 4, 40)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        path = graph_algo.shortest_path(37, 44)
        actual_path = nx.dijkstra_path(G, 37, 44)
        actual_dist = nx.dijkstra_path_length(G, 37, 44)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        list = graph_algo.connected_component(90)
        list_actual = []
        self.assertEqual(list, list_actual)
        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        self.assertEqual(list, list_actual)

        graph_algo.get_graph().remove_edge(29, 28)
        G.remove_edge(29, 28)
        list = graph_algo.connected_component(29)
        list_actual = [29]
        self.assertEqual(list, list_actual)
        list = graph_algo.connected_component(17)
        list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
        self.assertEqual(list, list_actual)
        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        list_actual = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        list_actual = [list_actual[1], list_actual[0]]
        self.assertEqual(list, list_actual)

        graph_algo.get_graph().remove_edge(15, 16)
        G.remove_edge(15, 16)
        graph_algo.get_graph().remove_edge(15, 39)
        G.remove_edge(15, 39)
        graph_algo.get_graph().remove_edge(15, 14)
        G.remove_edge(15, 14)
        list = graph_algo.connected_component(17)
        list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
        self.assertEqual(list, list_actual)
        list = graph_algo.connected_component(29)
        list_actual = [29]
        self.assertEqual(list, list_actual)
        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        list_actual = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        list_actual = [list_actual[2], list_actual[0], list_actual[1]]
        self.assertEqual(list, list_actual)

        graph_algo.get_graph().add_edge(15, 16, 1.8726071511162605)
        G.add_edge(15, 16)
        list = graph_algo.connected_component(15)
        list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                       28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
        self.assertEqual(list, list_actual)

    def test_json_a4(self):
        graph_algo = GraphAlgo()
        list = graph_algo.connected_component(8)
        list_actual = []
        self.assertEqual(list, list_actual)

        path = graph_algo.shortest_path(0, 1)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        list = graph_algo.connected_components()
        list_actual = []
        self.assertEqual(list, list_actual)

        graph = graph_algo.get_graph()
        file_path = "../data/A4"
        graph_algo.load_from_json(file_path)
        self.assertNotEqual(graph, graph_algo.get_graph())
        G = nx.DiGraph()
        for i in graph_algo.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph_algo.get_graph().get_all_v().keys():
            for j, w in graph_algo.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)

        path = graph_algo.shortest_path(0, 40)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        path = graph_algo.shortest_path(40, 2)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        path = graph_algo.shortest_path(38, 1)
        actual_path = nx.dijkstra_path(G, 38, 1)
        actual_dist = nx.dijkstra_path_length(G, 38, 1)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        path = graph_algo.shortest_path(26, 37)
        actual_path = nx.dijkstra_path(G, 26, 37)
        actual_dist = nx.dijkstra_path_length(G, 26, 37)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        graph_algo.get_graph().remove_edge(20, 19)
        G.remove_edge(20, 19)
        path = graph_algo.shortest_path(20, 19)
        actual_path = nx.dijkstra_path(G, 20, 19)
        actual_dist = nx.dijkstra_path_length(G, 20, 19)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        graph_algo.get_graph().add_edge(20, 19, 1.4313420158759202)
        G.add_edge(20, 19, weight = 1.4313420158759202)

        list = graph_algo.connected_component(90)
        list_actual = []
        self.assertEqual(list, list_actual)
        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        self.assertEqual(list, list_actual)

        graph_algo.get_graph().remove_edge(20, 19)
        G.remove_edge(20, 19)
        list = graph_algo.connected_component(0)
        list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
        self.assertEqual(list, list_actual)
        graph_algo.get_graph().remove_edge(20, 21)
        G.remove_edge(20, 21)
        list = graph_algo.connected_component(0)
        list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26,
                       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
        self.assertEqual(list, list_actual)
        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        list_actual = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        list_actual = [list_actual[1], list_actual[0]]
        self.assertEqual(list, list_actual)

        graph_algo.get_graph().remove_edge(7, 6)
        G.remove_edge(7, 6)
        graph_algo.get_graph().remove_edge(8, 9)
        G.remove_edge(8, 9)
        graph_algo.get_graph().remove_edge(35, 36)
        G.remove_edge(35, 36)
        graph_algo.get_graph().remove_edge(32, 31)
        G.remove_edge(32, 31)
        list = graph_algo.connected_component(27)
        list_actual = [0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 36, 37, 38, 39]
        self.assertEqual(list, list_actual)

        list = graph_algo.connected_component(32)
        list_actual = [7, 8, 32, 33, 34, 35]
        self.assertEqual(list, list_actual)

        #pass
        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        list_actual = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        # list_actual = [list_actual[2], list_actual[0], list_actual[1]]
        # self.assertEqual(list, list_actual)

    def test_json_a5(self):
        graph_algo = GraphAlgo()
        list = graph_algo.connected_component(8)
        list_actual = []
        self.assertEqual(list, list_actual)

        path = graph_algo.shortest_path(0, 1)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        list = graph_algo.connected_components()
        list_actual = []
        self.assertEqual(list, list_actual)

        graph = graph_algo.get_graph()
        file_path = "../data/A5"
        graph_algo.load_from_json(file_path)
        self.assertNotEqual(graph, graph_algo.get_graph())
        G = nx.DiGraph()
        for i in graph_algo.get_graph().get_all_v().keys():
            G.add_node(i)
        for i in graph_algo.get_graph().get_all_v().keys():
            for j, w in graph_algo.get_graph().all_out_edges_of_node(i).items():
                G.add_edge(i, j, weight=w)

        path = graph_algo.shortest_path(0, 48)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        path = graph_algo.shortest_path(80, 2)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        path = graph_algo.shortest_path(47, 35)
        actual_path = nx.dijkstra_path(G, 47, 35)
        actual_dist = nx.dijkstra_path_length(G, 47, 35)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        path = graph_algo.shortest_path(0, 32)
        actual_path = nx.dijkstra_path(G, 0, 32)
        actual_dist = nx.dijkstra_path_length(G, 0, 32)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        graph_algo.get_graph().remove_edge(13, 14)
        G.remove_edge(13, 14)
        path = graph_algo.shortest_path(13, 14)
        actual = (math.inf, [])
        self.assertEqual(actual, path)

        graph_algo.get_graph().add_edge(13, 14, 1.591436701981711)
        G.add_edge(13, 14, weight = 1.591436701981711)

        path = graph_algo.shortest_path(47, 21)
        actual_path = nx.dijkstra_path(G, 47, 21)
        actual_dist = nx.dijkstra_path_length(G, 47, 21)
        bol = False
        if (path[0] - actual_dist) < 0.001:
            bol = True
        self.assertTrue(bol)
        self.assertEqual(actual_path, path[1])

        list = graph_algo.connected_component(90)
        list_actual = []
        self.assertEqual(list, list_actual)
        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        self.assertEqual(list, list_actual)

        graph_algo.get_graph().remove_edge(13, 14)
        G.remove_edge(13, 14)
        list = graph_algo.connected_component(0)
        list_actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual(list, list_actual)
        list = graph_algo.connected_component(19)
        list_actual = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
        self.assertEqual(list, list_actual)

        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        list_actual = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        self.assertEqual(list, list_actual)

        graph_algo.get_graph().remove_edge(47, 46)
        G.remove_edge(47, 46)
        list = graph_algo.connected_component(47)
        list_actual = [47]
        self.assertEqual(list, list_actual)

        list = graph_algo.connected_component(19)
        list_actual = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
        self.assertEqual(list, list_actual)

        list = graph_algo.connected_components()
        nx_components = nx.strongly_connected_components(G)
        temp = []
        list_actual = []
        for n in nx_components:
            for i in n:
                temp.append(i)
            list_actual.append(temp)
            temp = []
        list_actual = [list_actual[0], list_actual[2], list_actual[1]]
        self.assertEqual(list, list_actual)


if __name__ == '__main__':
    unittest.main()