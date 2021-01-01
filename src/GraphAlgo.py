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
                for i in Nodes:
                    id = i.get("id")
                    if len(i) == 1:
                        list_random = [random.uniform(0.0, 3.0) for j in range(2)]
                        x, y = list_random
                        z = 0.0
                        pos = (x, y, z)
                        new_graph.add_node(id, pos)
                    else:
                        pos = i.get("pos")
                        new_graph.add_node(id, pos)

                for p in Edges:
                    src = p.get("src")
                    w = p.get("w")
                    dest = p.get("dest")
                    new_graph.add_edge(src, dest, w)

            self._graph = new_graph
            return True
        except Exception as e:
            print(e)
            return False






