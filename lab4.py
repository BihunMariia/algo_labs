def find_root_vertex(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices

    for start_vertex in range(num_vertices):
        if not visited[start_vertex]:
            queue = [start_vertex]
            while queue:
                current_vertex = queue[0]
                visited[current_vertex] = True
                unvisited_neighbors = [neighbor for neighbor in graph[current_vertex] if not visited[neighbor]]
                if unvisited_neighbors:
                    queue.append(unvisited_neighbors[0])
                else:
                    queue.pop()

            if all(visited):
                return start_vertex

    return -1

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()
    
    num_vertices = int(lines[0])
    graph = [[] for _ in range(num_vertices)]

    for line in lines[1:]:
        u, v = map(int, line.split())
        graph[u].append(v)

    root_vertex = find_root_vertex(graph)

    with open("output.txt", "w") as file:
        file.write(str(root_vertex))
