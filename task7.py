import sys

def min_cost_to_cross_river(n, cost, k, m):
    # Initialize a list to store the minimum cost to reach each platform
    dp = [sys.maxsize] * n

    # Base case: Cost to reach the starting platform is 0
    dp[0] = 0

    # Iterate through each platform
    for i in range(n):
        # Iterate through possible jumps (up to k)
        for j in range(1, k + 1):
            if i + j < n:
                # Update the minimum cost to reach the next platform
                dp[i + j] = min(dp[i + j], dp[i] + cost[i + j])

    # The minimum cost to reach the other side of the river is at the last platform
    return dp[-1]

# Example usage
n = 8
k = 4
m = 4
cost = [12, 5, 8, 9, 11, 13, 16, 1]

result = min_cost_to_cross_river(n, cost, k, m)
print("Minimum cost to cross the river:", result)
