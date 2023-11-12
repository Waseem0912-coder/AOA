def find_optimal_path(n, m, k, cost):
    # Initialize DP arrays for costs and paths
    dp_cost = [[float('inf')] * m for _ in range(n)]
    dp_path = [[[] for _ in range(m)] for _ in range(n)]

    # Initial platform cost and path
    dp_cost[0][0] = cost[0]
    dp_path[0][0] = [0]

    # Fill DP tables
    for i in range(1, n):
        for j in range(1, min(i + 1, m)):  # j cannot exceed i (number of jumps cannot be more than platforms visited)
            # Check all possible previous platforms within jump limit
            for p in range(max(0, i - k), i):
                if dp_cost[p][j - 1] != float('inf'):
                    new_cost = dp_cost[p][j - 1] + cost[i]
                    # Update if new path is cheaper
                    if new_cost < dp_cost[i][j]:
                        dp_cost[i][j] = new_cost
                        dp_path[i][j] = dp_path[p][j - 1] + [i]

    # The optimal path must use exactly m-1 jumps to reach the last platform
    if dp_cost[-1][m - 1] != float('inf'):
        return dp_path[-1][m - 1]
    else:
        return "No path found"
n = 8
k = 3 
m = 5
cost = [8, 9, 6, 3, 2, 5, 4, 1]


# Test the function with the given parameters
result = find_optimal_path(n, m, k, cost)
print(result)

