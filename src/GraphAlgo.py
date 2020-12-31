from src import GraphAlgoInterface
from typing import List
from src import GraphInterface
from DiGraph import DiGraph
from NodeData import NodeData
import json
import random

class GraphAlgo:

    def __init__(self):
        self._graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        return self._graph

    def as_dict_edge(self, src: int, dest: int, weight: float):
        self.edge = {"src": src, "w": weight, "dest": dest}
        return self.edge

    def save_to_json(self, file_name: str) -> bool:
        try:
            Nodes = []
            Edges = []
            for p in self._graph.get_all_v().keys():
                for k, v in self._graph.all_out_edges_of_node(p).items():
                    edge = self.as_dict_edge(p, k, v)
                    Edges.append(edge)
            for i in self._graph.get_all_v().values():
                node = i.as_dict_node()
                id = node["id"]
                pos = node["pos"]
                if pos is None:
                    node = {"id": id}
                else:
                    node = {"pos": pos, "id": id}
                Nodes.append(node)
            with open(file_name, "w") as file:
                json.dump({"Edges": Edges, "Nodes": Nodes}, fp=file)
            return True

        except Exception as e:
            print(e)
            return False

    def load_from_json(self, file_name: str) -> bool:
        new_graph = DiGraph()
        try:
            with open(file_name, "r") as file:
                json_data = file.read()
                my_dict = json.loads(json_data)
                Edges = my_dict["Edges"]
                Nodes = my_dict["Nodes"]
                for i in len(Nodes):
                    id = Nodes[i].get("id")
                    if len(Nodes[i]) == 1:
                        list_random = [random.uniform(0.0, 3.0) for j in range(3)]
                        (x, y, z) = list_random
                        new_graph.add_node(id, (x, y, z))
                    else:
                        pos = Nodes[i].get("pos")
                        new_graph.add_node(id, pos)

                for p in len(Edges):
                    src = Edges[p].get("src")
                    w = Edges[p].get("w")
                    dest = Edges[p].get("dest")
                    new_graph.add_edge(src, dest, w)

            self._graph = new_graph
            return True
        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    graphalgo = GraphAlgo()
    graph = graphalgo.get_graph()
    t0 = (1.2, 2.3, 3.3)
    t1 = (1.2, 2.3, 7.3)
    t2 = (1.2, 5.3, 3.6)
    t3 = (51.2, 2.3, 9.3)
    t4 = (8.2, 7.3, 3.2)
    for i in range(5):
        graph.add_node(i)
    graph.add_edge(0, 1, 2.3)
    graph.add_edge(0, 3, 1.2)
    graph.add_edge(1, 2, 4.5)
    graph.add_edge(1, 4, 4.9)
    graph.add_edge(3, 2, 1.34)
    graph.add_edge(2, 1, 4.5)

    graphalgo.save_to_json("check.json")
    graphalgo.load_from_json("check.json")
    print(graphalgo.get_graph())
    print("number of edges", graphalgo.get_graph().e_size())
    print(graphalgo.get_graph().get_all_v().get(2).getPos())
    print("0 ", graphalgo.get_graph().all_out_edges_of_node(0))
    print("0 ", graphalgo.get_graph().all_in_edges_of_node(0))
    print("1 ", graphalgo.get_graph().all_out_edges_of_node(1))
    print("1 ", graphalgo.get_graph().all_in_edges_of_node(1))
    print("2 ", graphalgo.get_graph().all_out_edges_of_node(2))
    print("2 ", graphalgo.get_graph().all_in_edges_of_node(2))
    print("3 ", graphalgo.get_graph().all_out_edges_of_node(3))
    print("3 ", graphalgo.get_graph().all_in_edges_of_node(3))
    print("4 ", graphalgo.get_graph().all_out_edges_of_node(4))
    print("4 ", graphalgo.get_graph().all_in_edges_of_node(4))
    print("mc ", graphalgo.get_graph().get_mc)
    list = [random.uniform(0.0, 3.0) for j in range(3)]
    print(type(list))
    (x, y, z) = list
    print(type((x, y, z) ))
    print((x, y, z))




