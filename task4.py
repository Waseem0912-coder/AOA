import sys
from collections import deque

def min_cost_linear_with_path(cost, k):
    n = len(cost)
    dp = [0] * n
    dq = deque()  # To store indices of platforms
    path = [[] for _ in range(n)]  # To store paths

    for i in range(n):
        # Remove platforms more than k steps away
        while dq and dq[0] < i - k:
            dq.popleft()

        # Cost to reach current platform
        dp[i] = cost[i] + (dp[dq[0]] if dq else 0)

        # Store the path
        path[i] = path[dq[0]] + [i] if dq else [i]

        # Maintain deque properties
        while dq and dp[i] <= dp[dq[-1]]:
            dq.pop()
        dq.append(i)

    # Find the index of the minimum cost within the last k elements
    min_cost_index = n - k + min(range(k), key=lambda x: dp[n-k+x])

    return dp[min_cost_index], path[min_cost_index]

# Reading input from stdin
first_line = sys.stdin.readline().strip()
n, k = map(int, first_line.split())

second_line = sys.stdin.readline().strip()
cost = list(map(int, second_line.split()))

min_cost, min_path = min_cost_linear_with_path(cost, k)

# Formatting output
output = ' '.join(map(str, min_path))
print(output)
