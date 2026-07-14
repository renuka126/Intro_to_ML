from collections import deque
locations = ['A', 'B', 'C', 'D', 'E']

def dfs(start, visited):
    print(locations[start], end=" ")
    visited[start] = True
    for i in range(len(adj_matrix[start])):
        if adj_matrix[start][i] == 1 and not visited[i]:
            dfs(i, visited)

adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbor in adj_list[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("Depth First Search (DFS) starting from A:")
visited = [False] * len(locations)
dfs(0, visited)

print("\n\nBreadth First Search (BFS) starting from A:")
bfs('A')
