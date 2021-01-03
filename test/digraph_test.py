import unittest
import random


from src.GraphInterface import GraphInterface
from src.node_data import node_data
from src.NodeData import NodeData
from src.DiGraph import DiGraph


class DiGraphTest(unittest.TestCase):

    def test_add_node(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        graph.add_node(1, (1, 2, 3))
        for i in range(10):
            self.assertEqual(graph.__contains__(i),  True)
        node1 = graph.get_all_v().get(1)
        self.assertEqual(node1.get_pos(), None)

    def test_remove_node(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        for i in range(1, 10, 2):
            graph.remove_node(i);
        for i in range(1, 10, 2):
            self.assertEqual(graph.__contains__(i), False)

    def test_add_edge(self):
        graph = DiGraph()
        for i in range(5):
            graph.add_node(i)
        test_dict = {"0": 3.4,"1": 3.5, "2": 5.4 , "3": 3.1, "4": 4.5}
        conn_dict = {"0": 1,"1": 2, "2": 3, "3": 4, "4": 0}
        for k in graph.get_all_v().keys():
            graph.add_edge(k, conn_dict[str(k)], test_dict[str(k)])
        for k, v in graph.get_all_v().items():
            weight = v.getWeight(conn_dict[str(k)])
            self.assertEqual(weight, test_dict[str(k)])

    def test_remove_edge(self):
        graph = DiGraph()
        for i in range(5):
            graph.add_node(i)
        weight_dict = {"0": 3.4, "1": 3.5, "2": 5.4, "3": 3.1, "4": 4.5}
        conn_dict = {"0": 1, "1": 2, "2": 3, "3": 4, "4": 0}
        remove_dict = {"0": False,"1": True, "2": False, "3": True, "4": False}
        for k in graph.get_all_v().keys():
            graph.add_edge(k, conn_dict[str(k)], weight_dict[str(k)])
        for k in range(0, 5, 2):
            graph.remove_edge(k, conn_dict[str(k)])
        for k in graph.get_all_v().keys():
            edge_dict = graph.all_out_edges_of_node(k);
            ans = edge_dict != {}
            self.assertEqual(ans, remove_dict[str(k)])

    def test_all_out_edges_of_node(self):
        graph = DiGraph()
        edges_list_tuple = []
        for i in range(5):
            graph.add_node(i)
        for s in graph.get_all_v().keys():
            for d in graph.get_all_v().keys():
                w = random.random()
                graph.add_edge(s, d, w)
                edges_list_tuple.append((s, d, w))
        for v in graph.get_all_v().keys():
            edges_list = [(s, d, w) for s, d, w in edges_list_tuple if d != s and s == v]
            edge_dict = graph.all_out_edges_of_node(v)
            for s, d, w in edges_list:
                self.assertEqual(edge_dict[d], w)

    def test_all_in_edges_of_node(self):
        graph = DiGraph()
        edges_list_tuple = []
        for i in range(5):
            graph.add_node(i)
        for s in graph.get_all_v().keys():
            for d in graph.get_all_v().keys():
                w = random.random()
                graph.add_edge(s, d, w)
                edges_list_tuple.append((s, d, w))
        for v in graph.get_all_v().keys():
            edges_list = [(s, d, w) for s, d, w in edges_list_tuple if d != s and d == v]
            edge_dict = graph.all_in_edges_of_node(v)
            for s, d, w in edges_list:
                self.assertEqual(edge_dict[s], w)

    def test_vertexes_size(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        self.assertEqual(graph.v_size(), 10)
        graph.add_node(1, (1, 2, 3))
        self.assertEqual(graph.v_size(), 10)
        for i in range(0, 10, 2):
            graph.remove_node(i);
        self.assertEqual(graph.v_size(), 5)

    def test_edge_size(self):
        graph = DiGraph()
        for i in range(5):
            graph.add_node(i)
        weight_dict = {"0": 3.4, "1": 3.5, "2": 5.4, "3": 3.1, "4": 4.5}
        conn_dict = {"0": 1, "1": 2, "2": 3, "3": 4, "4": 0}
        for k in graph.get_all_v().keys():
            graph.add_edge(k, conn_dict[str(k)], weight_dict[str(k)])
        self.assertEqual(graph.e_size(), 5)
        graph.add_edge(0, 1, 3.5)
        self.assertEqual(graph.e_size(), 5)
        for k in range(0, 5, 2):
            graph.remove_edge(k, conn_dict[str(k)])
        self.assertEqual(graph.e_size(), 2)
        graph.remove_edge(0, 1)
        self.assertEqual(graph.e_size(), 2)

    def test_MC(self):
        graph = DiGraph()
        for i in range(5):
            graph.add_node(i)
        weight_dict = {"0": 3.4, "1": 3.5, "2": 5.4, "3": 3.1, "4": 4.5}
        conn_dict = {"0": 1, "1": 2, "2": 3, "3": 4, "4": 0}
        self.assertEqual(graph.get_mc(), 5)
        for k in graph.get_all_v().keys():
            graph.add_edge(k, conn_dict[str(k)], weight_dict[str(k)])
        self.assertEqual(graph.get_mc(), 10)
        graph.add_edge(0, 1, 3.5)
        self.assertEqual(graph.get_mc(), 10)
        for k in range(0, 5, 2):
            graph.remove_edge(k, conn_dict[str(k)])
        self.assertEqual(graph.get_mc(), 13)
        graph.remove_edge(0, 1)
        self.assertEqual(graph.get_mc(), 13)
        graph.remove_node(0)
        self.assertEqual(graph.get_mc(), 14)
        graph.remove_node(0)
        self.assertEqual(graph.get_mc(), 14)


if __name__ == "__main__":
    unittest.main()
