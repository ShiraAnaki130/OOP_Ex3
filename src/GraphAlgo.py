from math import inf
import matplotlib.pyplot as plt
import numpy as np
from src.GraphAlgoInterface import GraphAlgoInterface
from typing import List
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph
from src.NodeData import NodeData
import json
import random
import queue


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None):
        if graph is None:
            self._graph = DiGraph()
        else:
            self._graph = graph
        self._parent = {}

    def get_graph(self) -> GraphInterface:
        """
        This function returns the graph on which this set of algorithms operates on.
        :return: A directional weighted graph.
        """
        return self._graph

    def as_dict_edge(self, src: int, dest: int, weight: float) -> dict:
        """"
        This function creates a dictionary of a single edge in the graph
        with the fields of src, dest and weight- according to the JSON format.
        @param src: the source of the edge
        @param dest: the destination of the edge
        @param weight: the edge's weight
        :return: the dictionary of this edge.
        """
        edge = {"src": src, "w": weight, "dest": dest}
        return edge

    def save_to_json(self, file_name: str) -> bool:
        """
        This function saves the graph in JSON format to a file.
        @param file_name: The path to the out file.
        @return: True if the save was successful, or Flase o.w.
        """
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
        """
        This function loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, or False o.w.
        """
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
                        new_graph.add_node(id, None)
                    else:
                        pos_str = i.get("pos")
                        x, y, z = pos_str.split(",")
                        pos_f = (float(x), float(y), float(z))
                        new_graph.add_node(id, pos_f)

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

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        this function check with dijkstra algorithm the shortest path between two nodes on the graph
        :param id1: source node id
        :param id2: destination node id
        :return : tuple of the distance of the edge in the graph and list of the nodes keys in the path.
        """
        priority_queue = queue.PriorityQueue()
        nodes = self._graph.get_all_v()
        if id1 == id2:
            if id1 in nodes.keys():
                return 0.0, [id1]
            else:
                return inf, []
        if id1 not in nodes.keys() or id2 not in nodes.keys():
            return inf, []
        parent = {}
        for n in nodes.values():
            n.set_tag(inf)
        start_node = nodes.get(id1)
        start_node.set_tag(0)
        priority_queue.put(start_node)
        while not priority_queue.empty():
            vertex = priority_queue.get()
            if vertex.get_key() != id2:
                edges = self._graph.all_out_edges_of_node(vertex.get_key())
                for e, v in edges.items():
                    node_e = nodes[e]
                    t = v + vertex.get_tag()
                    if t < node_e.get_tag():
                        node_e.set_tag(t)
                        priority_queue.put(node_e)
                        parent[e] = vertex.get_key()
            else:
                break
        path = []
        if id2 in parent.keys():
            node = id2
            path.append(node)
            while node != id1:
                node = parent[node]
                path.append(node)
            path.reverse()
        return nodes[id2].get_tag(), path

    def plot_graph(self) -> None:
        """
        This function plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
         """
        all_vertexes = self._graph.get_all_v()
        x_values = []
        y_values = []
        for i in all_vertexes.values():
            if i.get_pos():
                x_values.append(i.get_pos()[0])
                y_values.append(i.get_pos()[1])
            else:
                x_random = random.uniform(35.18, 35.2)
                y_random = random.uniform(32.1, 32.2)
                i.set_pos((x_random, y_random, 0.0))
                x_values.append(x_random)
                y_values.append(y_random)
        n = [j for j in all_vertexes.keys()]
        fig, ax = plt.subplots()
        ax.scatter(x_values, y_values)
        for p, txt in enumerate(n):
            ax.annotate(n[p], (x_values[p], y_values[p]))
        plt.plot(x_values, y_values, "C4o")
        for i in all_vertexes.keys():
            for j in self._graph.all_out_edges_of_node(i):
                x1_coordinate = all_vertexes.get(i).get_pos()[0]
                y1_coordinate = all_vertexes.get(i).get_pos()[1]
                x2_coordinate = all_vertexes.get(j).get_pos()[0]
                y2_coordinate = all_vertexes.get(j).get_pos()[1]
                if self._graph.v_size()<20:
                    plt.arrow(x1_coordinate, y1_coordinate, (x2_coordinate - x1_coordinate),(y2_coordinate - y1_coordinate), length_includes_head=True, width=0.000009, head_width=0.0011111112233, color='k')
                else:
                    plt.arrow(x1_coordinate, y1_coordinate, (x2_coordinate - x1_coordinate),
                              (y2_coordinate - y1_coordinate), length_includes_head=True, width=0.000003,
                              head_width=0.00016, color='k')
        plt.ylabel("y axis")
        plt.title("OOP_Ex3")
        plt.xlabel("x axis")
        plt.show()

    def bfs(self, id1: int) -> None:
        """
           this function implement the BFS algorithm
           :param id1: starting node id
        """
        nodes = self._graph.get_all_v()
        for n in nodes.values():
            n.set_tag(0)
        frontier = queue.Queue()
        start_node = nodes[id1]
        start_node.set_tag(1)
        frontier.put(start_node)
        while not frontier.empty():
            nxt = frontier.get()
            for e in self._graph.all_out_edges_of_node(nxt.get_key()):
                if nodes[e].get_tag() == 0:
                    nodes[e].set_tag(1)
                    frontier.put(nodes[e])
                    self._parent[e] = nxt.get_key()
            nxt.set_tag(2)

    def transpose_bfs(self, id1: int) -> None:
        """
           this function implement the BFS algorithm on transpose graph
           :param id1: starting node id
        """
        nodes = self._graph.get_all_v()
        for n in nodes.values():
            n.set_tag(0)
        frontier = queue.Queue()
        start_node = nodes[id1]
        start_node.set_tag(1)
        frontier.put(start_node)
        while not frontier.empty():
            nxt = frontier.get()
            for e in self._graph.all_in_edges_of_node(nxt.get_key()):
                if nodes[e].get_tag() == 0:
                    nodes[e].set_tag(1)
                    frontier.put(nodes[e])
                    self._parent[e] = nxt.get_key()
            nxt.set_tag(2)

    def connected_component(self, id1: int) -> list:
        """
            check Strongly Connected Component(SCC) of given node id
            with the intersection of BFS and transpose BFS algorithms
            :param id1: given node id
            :return: list of the keys that are Strongly Connected
        """
        if id1 in self._graph.get_all_v().keys():
            self._parent = {id1: None}
            self.bfs(id1)
            nodes_out = self._parent
            self._parent = {id1: None}
            self.transpose_bfs(id1)
            nodes_in = self._parent
            keys = [n for n in nodes_out.keys() if n in nodes_in.keys()]
            keys.sort()
            return keys
        return []

    def connected_components(self) -> List[list]:
        """
        create list of all check Strongly Connected Component(SCC) on the graph
        with the connected component function
        :return :list of all the connected components
        """
        nodes = self._graph.get_all_v()
        mark = []
        components = []
        for k in nodes.keys():
            if k not in mark:
                component = self.connected_component(k)
                mark[-1:-1] = component
                components.append(component)
        return components

    def __eq__(self, other):
        """
        This function is checking if this GraphAlgo and the other object is equals.
        :param other: another object
        :return: True if other is from the type of GraphAlgo and it equals to this GraphAlgo.
        """
        if not (isinstance(other, GraphAlgo)) or (other is None):
            return False
        return self._graph.__eq__(other.get_graph())


