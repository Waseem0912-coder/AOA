def min_cost_to_cross_river(n, platform_costs, k, m):
    # Memoization table, initialized to None
    memo = [[None for _ in range(m+1)] for _ in range(n)]

    def dp(i, j):
        # Base case: starting position
        if i == 0 and j == 0:
            return 0, [0]
        # Invalid cases
        if i < 0 or j <= 0:
            return float('inf'), []
        # Check memo table
        if memo[i][j] is not None:
            return memo[i][j]
        
        min_cost = float('inf')
        min_path = []
        # Check all possible previous platforms within jump limit
        for p in range(max(0, i - k), i):
            current_cost, current_path = dp(p, j - 1)
            current_cost += platform_costs[p]
            if current_cost < min_cost:
                min_cost = current_cost
                min_path = current_path + [i]

        memo[i][j] = (min_cost, min_path)
        return memo[i][j]

    # Find minimum cost among the last k platforms
    result = float('inf')
    final_path = []
    for i in range(n):
        if i + k >= n:  # Check if the jump can take you across the river
            current_cost, path = dp(i, m - 1)
            if current_cost < result:
                result = current_cost + platform_costs[i]
                final_path = path  # Do not add 'n' to the path

    return (result, final_path) if result != float('inf') else (-1, [])  # Return -1 if not possible

# Example usage
"""n = 8
m = 4
k = 4
platform_costs = [12, 5, 8, 9, 11, 13, 16, 1]"""

n = 8
k= 3
m =5
platform_costs = [8, 9, 6, 3, 2, 5, 4, 1]
min_cost, path = min_cost_to_cross_river(n, platform_costs, k, m)
print(min_cost, path)
