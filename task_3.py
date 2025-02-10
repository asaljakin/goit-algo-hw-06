from graph_creation import create_graph, add_weights
from graph_algorithms import dijkstra

# Створення графа з вагами
G = create_graph()
G = add_weights(G)

# Виконуємо алгоритм Дейкстри
start_node = "Kyiv"
shortest_paths = dijkstra(G, start_node)

print(f"Найкоротші шляхи від {start_node}: {shortest_paths}")
