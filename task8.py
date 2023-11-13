import sys

def find_optimal_path_optimized(n, m, k, cost):
    # Initialize DP arrays for costs and paths
    dp_cost = [[float('inf')] * m for _ in range(n)]
    dp_path = [[[] for _ in range(m)] for _ in range(n)]

    # Initial platform cost and path
    dp_cost[0][0] = cost[0]
    dp_path[0][0] = [0]

    # Fill DP tables
    for i in range(1, n):
        for j in range(1, min(i + 1, m)):
            prev_max_range = max(0, i - k)
            for p in range(prev_max_range, i):
                if dp_cost[p][j - 1] != float('inf'):
                    new_cost = dp_cost[p][j - 1] + cost[i]
                    if new_cost < dp_cost[i][j]:
                        dp_cost[i][j] = new_cost
                        dp_path[i][j] = dp_path[p][j - 1] + [i]

    if dp_cost[-1][m - 1] != float('inf'):
        return dp_path[-1][m - 1]
    else:
        return "No path found"

def main():
    # Reading input from stdin
    first_line = sys.stdin.readline().strip()
    n, k, m = map(int, first_line.split())

    second_line = sys.stdin.readline().strip()
    cost = list(map(int, second_line.split()))

    result = find_optimal_path_optimized(n, m, k, cost)

    if isinstance(result, list):
        output = ' '.join(map(str, result))
        print(output)
    else:
        print(result)

if __name__ == "__main__":
    main()
