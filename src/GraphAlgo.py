import json
import random
import matplotlib.pyplot as plt
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self._graph = graph

    def get_graph(self) -> GraphInterface:
        """
        This function returns the graph on which this set of algorithms operates on.
        :return: A directional weighted graph.
        """
        return self._graph

    def as_dict_edge(self, src: int, dest: int, weight: float):
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
                plt.arrow(x1_coordinate, y1_coordinate, (x2_coordinate - x1_coordinate), (y2_coordinate - y1_coordinate), length_includes_head=True, width=0.000003, head_width=0.00016, color = 'k')
        plt.ylabel("y axis")
        plt.title("OOP_Ex3")
        plt.xlabel("x axis")
        plt.show()





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
    list = [random.uniform(35.1, 35.2) for j in range(3)]
    (x, y, z) = list
    t = (2.0, 7.9, 8.0)
    print((x, y, z))
    print("kk", type(t[0]))
    n = [i for i in graph.get_all_v().keys()]
    print("n ", n)
    graphalgo.plot_graph()
    pos = graph.get_all_v().get(0).get_pos()
    print("pos ", pos)
    print(type(pos))


    number = "35.18869800968523,32.104927164705884,0.0"
    x, y, z = number.split(",")
    pos1 = (float(x), float(y), float(z))
    print('pos ',pos1)
    print(type(pos1), type(pos1[0]), pos1[0])
    #print("x,y,z ", x, y, z)
    #print("num", type(number_1))
    #print("number_1", type(number_1), number_1)

    graph_new = DiGraph()
    for i in range(5):
        graph_new.add_node(i)
    graph_new.add_edge(0, 1, 2.3)
    graph_new.add_edge(0, 3, 1.2)
    graph_new.add_edge(1, 2, 4.5)
    graph_new.add_edge(1, 4, 4.9)
    graph_new.add_edge(3, 2, 1.34)
    graph_new.add_edge(2, 1, 4.5)
    print(graph.__dict__ )
    print(graph_new.__dict__ )
    if graph == graph_new:
        print("trueeee")
    else:
        print("f")
    list_1 = (7.8, [9, 0, 7])
    list_2 = (7.8, [9, 0, 7])
    if list_1 == list_2:
        print("eq")














