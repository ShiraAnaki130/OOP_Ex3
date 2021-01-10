import unittest

from src.NodeData import NodeData


class NodeDataTest(unittest.TestCase):

    def test_new_node(self):
        pos = (1, 2, 3)
        node1 = NodeData(1, pos, 3.4)
        self.assertEqual(node1.get_key(), 1)
        self.assertEqual(node1.get_pos(), (1, 2, 3))
        self.assertEqual(node1.get_weight(), 3.4)
        self.assertEqual(node1.get_info(), "f")
        self.assertEqual(node1.get_tag(), 0)
        self.assertEqual(node1.get_dest(), {})
        self.assertEqual(node1.get_src(), {})
        node2 = NodeData(2)
        self.assertEqual(node2.get_key(), 2)
        self.assertEqual(node2.get_pos(), None)
        self.assertEqual(node2.get_weight(), 0.0)
        self.assertEqual(node2.get_info(), "f")
        self.assertEqual(node2.get_tag(), 0)
        self.assertEqual(node2.get_dest(), {})
        self.assertEqual(node2.get_src(), {})

    def test_as_dict_node(self):
        pos = (1, 2, 3)
        node1 = NodeData(1, pos, 3.4)
        node_dict = node1.as_dict_node()
        test_dict = {"id": 1, "pos": pos, "_weight": 3.4, "_tag": 0, "_info": "f", "_src": {}, "_dest": {}}
        for k, v in node_dict.items():
            self.assertEqual(v, test_dict[k])

    def test_add_dest(self):
        pos = (1, 2, 3)
        node = NodeData(1, pos, 3.4)
        node.add_dest(1, 3.2)
        node.add_dest(2, 3.2)
        node.add_dest(3, 4.5)
        node.add_dest(4, 1.3)
        node_dict = node.get_dest()
        self.assertEqual(1 in node_dict, False)
        test_dict = {'2': 3.2, '3': 4.5, '4': 1.3}
        for k, v in node_dict.items():
            self.assertEqual(v, test_dict[str(k)])

    def test_has_dest(self):
        pos = (1, 2, 3)
        node = NodeData(1, pos, 3.4)
        node.add_dest(1, 3.2)
        node.add_dest(2, 3.2)
        node.add_dest(3, 4.5)
        node.add_dest(4, 1.3)
        test_list = [1, 2, 3, 4, 5]
        for k in test_list:
            if k == 1 or k == 5:
                self.assertEqual(node.has_dest(k), False)
            else:
                self.assertEqual(node.has_dest(k), True)

    def test_add_src(self):
        pos = (1, 2, 3)
        node = NodeData(1, pos, 3.4)
        node.add_src(1, 3.2)
        node.add_src(2, 3.2)
        node.add_src(3, 4.5)
        node.add_src(4, 1.3)
        node_dict = node.get_src()
        self.assertEqual(1 in node_dict, False)
        test_dict = {'2': 3.2, '3': 4.5, '4': 1.3}
        for k, v in node_dict.items():
            self.assertEqual(v, test_dict[str(k)])

    def test_has_src(self):
        pos = (1, 2, 3)
        node = NodeData(1, pos, 3.4)
        node.add_src(1, 3.2)
        node.add_src(2, 3.2)
        node.add_src(3, 4.5)
        node.add_src(4, 1.3)
        test_list = [1, 2, 3, 4, 5]
        for k in test_list:
            if k == 1 or k == 5:
                self.assertEqual(node.has_src(k), False)
            else:
                self.assertEqual(node.has_src(k), True)

    def test_remove_dest(self):
        pos = (1, 2, 3)
        node = NodeData(1, pos, 3.4)
        node.add_dest(2, 3.2)
        node.add_dest(3, 4.5)
        node.add_dest(4, 1.3)
        node.add_dest(5, 3.4)
        node.add_dest(6, 2.3)
        test_dict = {'2': True, '3': False, '4': True, '5': False, '6': True}
        for k in test_dict.keys():
            self.assertEqual(node.has_dest(int(k)), True)
        node.remove_dest(3)
        node.remove_dest(5)
        for k, v in test_dict.items():
            self.assertEqual(node.has_dest(int(k)), v)
        self.assertEqual(node.remove_dest(1), False)

    def test_remove_src(self):
        pos = (1, 2, 3)
        node = NodeData(1, pos, 3.4)
        node.add_src(2, 3.2)
        node.add_src(3, 4.5)
        node.add_src(4, 1.3)
        node.add_src(5, 3.4)
        node.add_src(6, 2.3)
        test_dict = {'2': True, '3': False, '4': True, '5': False, '6': True}
        for k in test_dict.keys():
            self.assertEqual(node.has_src(int(k)), True)
        node.remove_src(3)
        node.remove_src(5)
        for k, v in test_dict.items():
            self.assertEqual(node.has_src(int(k)), v)
        self.assertEqual(node.remove_src(1), False)

    def test_get_edge_weight(self):
        pos = (1, 2, 3)
        node = NodeData(1, pos, 3.4)
        node.add_dest(1, 3.2)
        node.add_dest(2, 3.2)
        node.add_dest(3, 4.5)
        node.add_dest(4, 1.3)
        node.add_dest(5, 3.4)
        node.add_dest(6, 2.3)
        test_dict = {'1': None, '2': 3.2, '3': 4.5, '4': 1.3, '5': 3.4, '6': 2.3}
        for k, v in test_dict.items():
            self.assertEqual(node.getWeight(int(k)), v)


if __name__ == "__main__":
    unittest.main()
