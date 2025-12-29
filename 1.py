def main():
    with open('27_1.txt', 'r') as f:
        n = int(f.readline().strip())
        A = []
        for i in range(n):
            row = list(map(int, f.readline().split()))
            A.append(row)

    MAX_DEPTH = 6

    for start in range(n):
        visited = [False] * n
        visited[start] = True
        path = [start]
        result = dfs(start, start, path, visited, 0, A, n, 1, MAX_DEPTH)
        if result is not None:
            k = len(result) - 1
            sequence = [str(x + 1) for x in result[:-1]]
            print(k)
            print(" ".join(sequence))
            return

    print("Нет")


def dfs(current, start, path, visited, current_sum, A, n, depth, max_depth):
    if depth > max_depth:
        return None

    if depth > 1:
        cycle_sum = current_sum + A[current][start]
        if cycle_sum < 0:
            return path + [start]

    for next_node in range(n):
        if not visited[next_node]:
            visited[next_node] = True
            path.append(next_node)
            new_sum = current_sum + A[current][next_node]
            result = dfs(next_node, start, path, visited, new_sum, A, n, depth + 1, max_depth)
            if result is not None:
                return result
            path.pop()
            visited[next_node] = False

    return None


main()