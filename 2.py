def main():
    with open('27_2.txt', 'r') as f:
        n = int(f.readline().strip())

        matrix1 = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            matrix1.append(row)

        matrix2 = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            matrix2.append(row)

    components1 = count_components(matrix1, n)
    components2 = count_components(matrix2, n)

    if components1 == components2:
        print("Да")
    else:
        print("Нет")


def dfs(node, visited, graph, n):
    visited[node] = True
    for neighbor in range(n):
        if graph[node][neighbor] == 1 and not visited[neighbor]:
            dfs(neighbor, visited, graph, n)


def count_components(graph, n):
    visited = [False] * n
    count = 0
    for node in range(n):
        if not visited[node]:
            dfs(node, visited, graph, n)
            count += 1
    return count


main()