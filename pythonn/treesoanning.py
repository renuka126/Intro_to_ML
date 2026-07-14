INF = 9999999  # Represents infinity
V = 5  # Number of locations (including pizza shop)

# Graph represented as adjacency matrix (travel time between locations)
G = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

selected = [False] * V  # To track selected nodes
no_edge = 0  # Count of edges in MST

selected[0] = True  # Start from the pizza shop (source node)

print("Edge : Time")
total_time = 0

# Loop until we have V-1 edges in MST
while no_edge < V - 1:
    minimum = INF
    x = 0
    y = 0

    for i in range(V):
        if selected[i]:
            for j in range(V):
                if (not selected[j]) and G[i][j]:
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x, y = i, j

    print(f"{x} - {y} : {G[x][y]}")
    total_time += G[x][y]
    selected[y] = True
    no_edge += 1

print("\nMinimum Total Delivery Time:", total_time)