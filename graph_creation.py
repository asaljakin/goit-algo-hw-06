import networkx as nx

def create_graph():
    G = nx.Graph()
    cities = ["Kyiv", "Lviv", "Odesa", "Kharkiv", "Dnipro"]
    edges = [
        ("Kyiv", "Lviv"),
        ("Kyiv", "Odesa"),
        ("Kyiv", "Kharkiv"),
        ("Kyiv", "Dnipro"),
        ("Lviv", "Odesa"),
        ("Odesa", "Dnipro"),
        ("Kharkiv", "Dnipro")
    ]
    G.add_nodes_from(cities)
    G.add_edges_from(edges)
    return G

def analyze_graph(G):
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degrees = dict(G.degree())
    average_degree = sum(degrees.values()) / num_nodes
    return num_nodes, num_edges, degrees, average_degree

def add_weights(G):
    edges_with_weights = [
        ("Kyiv", "Lviv", 5),
        ("Kyiv", "Odesa", 6),
        ("Kyiv", "Kharkiv", 3),
        ("Kyiv", "Dnipro", 4),
        ("Lviv", "Odesa", 8),
        ("Odesa", "Dnipro", 2),
        ("Kharkiv", "Dnipro", 7)
    ]
    G.add_weighted_edges_from(edges_with_weights)
    return G
