# OOP_Ex3 ![](data/oop3.jpg)

## About the project:

The project is about programming a data structure called a directional weighted graph in python.

The project code is basically a 'translation' from the OOP_Ex2 project's code, which about programming a directional weighted graph in Java.

### About the graph:

***description:***

The directional weighted graph is a data structure in which every edge has a direction and a weight (positive number).
This data structure contains vertexes from the type of node_data.

For creating the graph we program tree new classes-  NodeData, DiGraph, and GraphAlgo -every class implements an interface, which includes functions.

**NodeData:**

This class implements the functions of the interface called 'node_data'.

Every node_data has a unique key, a position in space, weight, tag and info(remark fields), and two dictionaries:

'dest'(key, weight): containing all the edges which getting out of this vertex

'src'(key, weight): containing all the edges which getting in of this vertex.

The functions which applicable on a vertex:

- add_dest(dest: int, weight: float): connecting an edge between self --> dest with the given weight.

- add_src(src: int, weight: float): connecting an edge between src --> self with the given weight. 

- has_dest(dest: int, weight: float = None): checking if there is an  edge between self--> dest with the given weight.

- has_src(src: int): checking if there is an edge between src--> self with the given weight.

- remove_dest(dest: int): removing the given dest from the 'dest' dictionary.

- remove_src(src: int): removing the given src from the 'src' dictionary.

- get_dest(): return a dictionary (key, weight) of all the edges which getting out of this vertex.

- get_src():  return a dictionary (key, weight) of all the edges which getting in of this vertex.

- getWeight(dest: int): return the edge's weight between  self--> dest.

- get_key(): return the vertex's key.

- set_key(id: int): sets a new key to the vertex.

- get_pos(): returns the position of the vertex.

- set_pos():  sets the position of the vertex.

- get_weight(): returns the vertex's weight

- set_weight():  sets a new weight for the vertex.

- get_tag(): returns the vertex's tag .

- set_tag(): sets a new tag to the vertex.

- get_tag(): returns the vertex's info .

- set_tag(): sets a new info to the vertex.

**DiGraph:**

