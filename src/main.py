from src.DiGraph import DiGraph
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import time
import networkx as nx


def runtime_nx(v, e):
    our_graph_algo = GraphAlgo()
    start_time = time.time()
    our_graph_algo.load_from_json("../data/G_{}_{}_0.json".format(v,e))
    end_time = time.time()
    our_time_load = end_time - start_time
    graph = our_graph_algo.get_graph()
    start_time = time.time()
    nx_graph = nx.DiGraph()
    for i in graph.get_all_v().keys():
        nx_graph.add_node(i)
    for i in graph.get_all_v().keys():
        for j, w in graph.all_out_edges_of_node(i).items():
            nx_graph.add_edge(i, j, weight=w)
    end_time = time.time()
    nx_time_load = end_time - start_time
    print("end load graph G_{}_{}_0   our time : {}    networkx time : {}".format(v,e,our_time_load, nx_time_load))
    start_time = time.time()
    our_graph_algo.connected_components()
    end_time = time.time()
    our_time_components = end_time - start_time
    start_time = time.time()
    nx_components = nx.strongly_connected_components(nx_graph)
    for n in nx_components:
        pass
    end_time = time.time()
    nx_time_components = end_time - start_time
    print("""end connected components algorithm on graph G_{}_{}_0  our time : {}   networkx time : {}""".format(
        v, e, our_time_components, nx_time_components))
    start_time = time.time()
    our_graph_algo.shortest_path(0, graph.v_size() - 1)
    end_time = time.time()
    our_time_shortest_path = end_time - start_time
    start_time = time.time()
    nx.dijkstra_path(nx_graph, 0, graph.v_size() - 1)
    nx.dijkstra_path_length(nx_graph, 0, graph.v_size() - 1)
    end_time = time.time()
    nx_time_shortest_path = end_time - start_time
    print("""end shortest_path algorithm on graph G_{}_{}_0 our time : {}  networkx time : {}""".format(
        v, e, our_time_shortest_path, nx_time_shortest_path))


def runtime(v,e):
    graph_algo = GraphAlgo()
    start_time = time.time()
    graph_algo.load_from_json("../data/G_{}_{}_0.json".format(v, e))
    end_time = time.time()
    time_load = end_time - start_time
    print("end load graph G_{}_{}_0    time : {} ".format(v, e, time_load,))
    graph = graph_algo.get_graph()
    start_time = time.time()
    graph_algo.connected_component(0)
    end_time = time.time()
    time_component = end_time - start_time
    print("""end connected component algorithm for node 0  on graph G_{}_{}_0 time : {}  """.format(
        v, e, time_component))
    start_time = time.time()
    graph_algo.connected_components()
    end_time = time.time()
    time_components = end_time - start_time
    print("""end connected components algorithm on graph G_{}_{}_0 time : {}  """.format(
        v, e, time_components,))
    start_time = time.time()
    shortest_path = graph_algo.shortest_path(0, graph.v_size() - 1)
    end_time = time.time()
    time_shortest_path = end_time - start_time
    print("""end shortest_path algorithm on graph G_{}_{}_0  time : {}  """.format(
        v, e, time_shortest_path))

def main():
    runtime_nx(10,80)
    runtime_nx(100, 800)
    runtime_nx(1000, 8000)
    runtime_nx(10000, 80000)
    runtime_nx(20000, 160000)
    runtime_nx(30000, 240000)

    runtime(10, 80)
    runtime(100, 800)
    runtime(1000, 8000)
    runtime(10000, 80000)
    runtime(20000, 160000)
    runtime(30000, 240000)


if __name__ == "__main__":
    main()
