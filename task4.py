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

"""# Example usage
n = 8  # Number of platforms
k = 4   # Maximum jump length
cost = [12, 5, 8, 9, 11, 13, 16, 1]  # Given cost for each platform
"""
n = 8
k = 3 
cost = [8, 9, 6, 3, 2, 5, 4, 1]

min_cost, min_path = min_cost_linear_with_path(cost, k)
print('Minimum cost:', min_cost)
print('Minimum cost path:', min_path)
