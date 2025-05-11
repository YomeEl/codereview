def topological_sort(graph, n):
    visited = [False] * n):
    visited = [False] * n
    rec_stack = [False] * n
    result = []
    
    def dfs(v):
        if rec_stack[v]:
            return False
        if visited[v]:
            return True
        visited[v] = True
        rec_stack[v] = True
        
        for i in range(n):
            if graph[v][i] != 0 and not dfs(i):
                return False
        
        rec_stack[v] = False
        result.append(v)
        return True
    
    for i in range(n):
        if not visited[i]:
            if not dfs(i):
                return "No solution"
    
    return [v + 1 for v in reversed(result)]


def read_graph(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        graph = []
        for _ in range(n):
            graph.append(list(map(int, f.readline().strip().split())))
    return graph, n


filename = "FileName.txt"
graph, n = read_graph(filename)
solution = topological_sort(graph, n)

if solution == "No solution":
    print(solution)
else:
   
