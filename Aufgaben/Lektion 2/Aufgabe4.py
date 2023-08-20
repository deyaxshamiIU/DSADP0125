import random

# Anzahl der Knoten im Graphen
N = 50

# Anzahl der Verbindungen
num_connections = 100

# Erzeugung einer leeren Matrix für den Graphen
graph_matrix = [[0] * N for _ in range(N)]

# Zufällige Erzeugung von Verbindungen
for _ in range(num_connections):
    source_node = random.randint(0, N - 1)
    target_node = random.randint(0, N - 1)

    # Stelle sicher, dass eine Verbindung nicht von einem Knoten zu sich selbst geht
    while target_node == source_node:
        target_node = random.randint(0, N - 1)

    graph_matrix[source_node][target_node] = 1

# Funktion zur Darstellung der Matrix
def print_graph_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

# Ausgabe der generierten Matrix
print("Generierter Graph:")
print_graph_matrix(graph_matrix)