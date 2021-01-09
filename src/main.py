from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import time

def main():
    graph_algo = GraphAlgo()
    start_time = time.time()
    graph_algo.load_from_json("../data/G_30000_240000_0.json")
    end_time = time.time()
    print(end_time-start_time)
    start_time = time.time()
    component = graph_algo.connected_component(0)
    end_time = time.time()
    # print(component)
    print(end_time - start_time)
    start_time = time.time()
    components = graph_algo.connected_components()
    end_time = time.time()
    # print(components)
    print(end_time - start_time)

if __name__ == "__main__":
    main()