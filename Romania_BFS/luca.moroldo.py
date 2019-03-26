import networkx as nx
from networkx.exception import NetworkXError

def romania():
    node_list = ["Bucharest", "Giurgiu", "Urziceni", "Hirsova", "Eforie", "Neamt", "Oradea", "Zerind", "Arad",
                 "Timisoara", "Lugoj", "Mehadia", "Dobreta", "Craiova", "Sibiu", "Fagaras", "Pitesti", "Rimnicu Vilcea",
                 "Vaslui", "Iasi"]

    graph = nx.Graph()

    for i in node_list:
        graph.add_node(i, percorso=[], visitato=False, f=0)

    graph.add_edge("Arad", "Zerind", weight=75)
    graph.add_edge("Arad", "Timisoara", weight=118)
    graph.add_edge("Arad", "Sibiu", weight=140)
    graph.add_edge("Zerind", "Oradea", weight=71)
    graph.add_edge("Mehadia", "Lugoj", weight=70)
    graph.add_edge("Mehadia", "Dobreta", weight=75)
    graph.add_edge("Craiova", "Dobreta", weight=120)
    graph.add_edge("Craiova", "Rimnicu Vilcea", weight=146)
    graph.add_edge("Craiova", "Pitesti", weight=138)
    graph.add_edge("Pitesti", "Rimnicu Vilcea", weight=97)
    graph.add_edge("Pitesti", "Bucharest", weight=101)
    graph.add_edge("Timisoara", "Lugoj", weight=111)
    graph.add_edge("Sibiu", "Fagaras", weight=99)
    graph.add_edge("Bucharest", "Fagaras", weight=211)
    graph.add_edge("Bucharest", "Giurgiu", weight=90)
    graph.add_edge("Bucharest", "Urziceni", weight=85)
    graph.add_edge("Vaslui", "Urziceni", weight=142)
    graph.add_edge("Vaslui", "Iasi", weight=92)
    graph.add_edge("Neamt", "Iasi", weight=87)
    graph.add_edge("Hirsova", "Urziceni", weight=98)
    graph.add_edge("Hirsova", "Eforie", weight=86)
    graph.add_edge("Sibiu", "Rimnicu Vilcea", weight=80)
    graph.add_edge("Sibiu", "Oradea", weight=151)

    return graph


def ampiezza(grafo, start, end):
    '''
    Apply BFS to find the path from a node to another
    :param grafo: networkx.Graph 
    :param start: name of start node
    :param end: name of destination node
    :return: Path from start to end if exists, empty list otherwise
    '''
    if nx.is_empty(grafo) or not grafo.has_node(start) or not grafo.has_node(end) or start == end:
        return []
    queue = [start]
    while queue:
        curr = queue.pop(0)
        for node in grafo.neighbors(curr):
            # skip iteration if node already visited
            if grafo.nodes[node]['visitato']:
                continue
            if node == end:
                return grafo.nodes(data=True)[curr]['percorso'] + [node]
            else:
                grafo.nodes[node]['percorso'] = grafo.nodes[curr]['percorso'] + [node]
                grafo.nodes[node]['visitato'] = True
                queue.append(node)
    # no path found
    return []
    

