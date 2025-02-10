# import networkx as nx
# import matplotlib.pyplot as plt

# # Створення графа
# G = nx.Graph()

# # Додавання вершин (станцій метро)
# stations = ["Станція A", "Станція B", "Станція C", "Станція D", "Станція E"]
# G.add_nodes_from(stations)

# # Додавання ребер (з'єднань між станціями)
# edges = [("Станція A", "Станція B"), ("Станція B", "Станція C"),
#          ("Станція C", "Станція D"), ("Станція D", "Станція E"),
#          ("Станція A", "Станція D")]
# G.add_edges_from(edges)

# # Візуалізація графа
# pos = nx.spring_layout(G)  # Розташування вершин
# nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
# plt.title("Транспортна мережа міста")
# plt.show()

# # Аналіз характеристик
# print("Кількість вершин:", G.number_of_nodes())
# print("Кількість ребер:", G.number_of_edges())
# print("Ступені вершин:", dict(G.degree()))
from graph_creation import create_graph, analyze_graph
import matplotlib.pyplot as plt
import networkx as nx

# Створення графа та його аналіз
G = create_graph()
num_nodes, num_edges, degrees, average_degree = analyze_graph(G)

# Візуалізація графа
plt.figure(figsize=(10, 6))
nx.draw(G, with_labels=True, node_color="skyblue", node_size=2000, edge_color="gray", font_size=15, font_weight="bold")
plt.title("Транспортна мережа міст України")
plt.show()

# Виведення результатів аналізу
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступінь вершин: {degrees}")
print(f"Середній ступінь вершини: {average_degree:.2f}")