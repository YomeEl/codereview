from collections import defaultdict

def dfs(vertex, visited, graph, result):
    if visited[vertex] == 1:
        return False # Cycle detected
    
    if visited[vertex] != 2:
        visited[vertex] = 1 # Mark vertex as being processed
        
        for neighbor in sorted(graph[vertex], reverse=True): # Sort neighbors in descending order
            if not dfs(neighbor, visited, graph, result):
                return False
                
        visited[vertex] = 2 # Mark vertex as fully processed
        result.append(vertex)
    
    return True

def topological_sort(FileName):
    with open(FileName, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        adjacency_matrix = [[int(x) for x in line.strip().split()] for line in lines[1:n+1]]

    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j]:
                graph[i].append(j)

    visited = [0]*n # 0: unvisited, 1: visiting, 2: visited
    result = []

    for v in reversed(range(n)): # Start from highest index vertices first
        if visited[v] == 0 and not dfs(v, visited, graph, result):
            print("No solution")
            return

    print(' '.join(map(str, reversed(result))))

# Example usage
print("Valid DAG, multiple solutions, one possible output")
topological_sort("FileName1")
print("Graph with cycle, should output \"No solution\"")
topological_sort("FileName2")
print("Valid DAG, vertices should be processed in descending order when possible")
topological_sort("FileName3")