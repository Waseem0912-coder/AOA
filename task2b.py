def min_cost_rec(cost, k):
    n = len(cost)
    memo = [None] * n
    prev = [-1] * n

    def dp(i):
        if i == 0:
            return cost[0]
        if memo[i] is not None:
            return memo[i]

        min_cost = float('inf')
        for j in range(1, min(i, k) + 1):
            current_cost = dp(i - j) + cost[i]
            if current_cost < min_cost:
                min_cost = current_cost
                prev[i] = i - j

        memo[i] = min_cost
        return min_cost

    # Find the end platform that gives minimum cost to cross the river
    min_cost = min(dp(i) for i in range(n - k, n))

    # Find the corresponding end platform
    end_platform = next(i for i in range(n - k, n) if memo[i] == min_cost)

    # Reconstruct the path
    path = []
    while end_platform != -1:
        path.append(end_platform)
        end_platform = prev[end_platform]
    path.reverse()

    return min_cost, path

# Example usage
n = 8  # Number of platforms
k = 4   # Maximum jump length
cost = [12, 5, 8, 9, 11, 13, 16, 1]  # Given cost for each platform

min_cost, path = min_cost_rec(cost, k)
print('Minimum cost:', min_cost)
print('Path with minimum cost:', ', '.join(map(str, path)))
