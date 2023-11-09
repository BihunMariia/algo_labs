def find_root_vertex(graph):
    def dfs(v, visited):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor, visited)

    num_vertices = len(graph)
    visited = [False] * num_vertices

    for vertex in range(num_vertices):
        if not visited[vertex]:
            dfs(vertex, visited)
            if all(visited):
                return vertex

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
