import sys

def min_cost_bottom_up(cost, k):
    n = len(cost)
    dp = [float('inf')] * n
    dp[0] = cost[0]

    for i in range(1, n):
        for j in range(max(0, i-k), i):
            if dp[j] + cost[i] < dp[i]:
                dp[i] = dp[j] + cost[i]

    min_cost = min(dp[-k:])  # Minimum cost in the last k platforms

    # Path reconstruction
    path = []
    for i in range(n - 1, -1, -1):
        if dp[i] == min_cost:
            path.append(i)
            min_cost -= cost[i]

    path.reverse()
    return dp[-1], path

# Reading input from stdin
first_line = sys.stdin.readline().strip()
n, k = map(int, first_line.split())

second_line = sys.stdin.readline().strip()
cost = list(map(int, second_line.split()))

min_cost, path = min_cost_bottom_up(cost, k)

# Formatting output
output = ' '.join(map(str, path))
print(output)
