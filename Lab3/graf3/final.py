def topological_sort(filename):
    with open(filename, "r") as f:
        n = int(f.readline())
        graph = [list(map(int, f.readline().split())) for _ in range(n)]

    visited = [0] * n
    result = []
    is_possible = True

    def dfs(u):
        nonlocal is_possible
        if not is_possible:
            return
        visited[u] = 1
        for v in sorted(range(n), reverse=True):
            if graph[u][v] != 0:
                if visited[v] == 1:
                    is_possible = False
                    return
                elif visited[v] == 0:
                    dfs(v)
        visited[u] = 2
        result.append(u)

    for u in sorted(range(n), reverse=True):
        if visited[u] == 0:
            dfs(u)
            if not is_possible:
                break

    if is_possible:
        print(" ".join(map(str, reversed(result))))
    else:
        print("No solution")


if __name__ == "__main__":
    print("Valid DAG, multiple solutions, one possible output")
    print(topological_sort("FileName1"))
    print('Graph with cycle, should output "No solution"')
    print(topological_sort("FileName2"))
    print("Valid DAG, vertices should be processed in descending order when possible")
    print(topological_sort("FileName3"))
