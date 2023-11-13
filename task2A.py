import sys

def min_cost_dp_with_path(cost, k):
    n = len(cost)
    dp = [float('inf')] * n
    prev = [-1] * n
    dp[0] = cost[0]

    for i in range(1, n):
        for j in range(1, min(k, i) + 1):
            if dp[i] > dp[i - j] + cost[i]:
                dp[i] = dp[i - j] + cost[i]
                prev[i] = i - j

    # Find the end platform that gives minimum cost to cross the river
    min_cost, end_platform = float('inf'), -1
    for i in range(n - k, n):
        if dp[i] < min_cost:
            min_cost = dp[i]
            end_platform = i

    # Reconstruct the path
    path = []
    while end_platform != -1:
        path.append(end_platform)
        end_platform = prev[end_platform]
    path.reverse()

    return min_cost, path

# Reading input from stdin
first_line = sys.stdin.readline().strip()
n, k = map(int, first_line.split())

second_line = sys.stdin.readline().strip()
cost = list(map(int, second_line.split()))

min_cost, path = min_cost_dp_with_path(cost, k)

# Formatting output
output = ' '.join(map(str, path))
print(output)
