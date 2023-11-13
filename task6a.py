import sys

def min_cost_to_cross_river(n, platform_costs, k, m):
    # Memoization table, initialized to None
    memo = [[None for _ in range(m + 1)] for _ in range(n)]

    def dp(i, j):
        # Base case and invalid cases
        if i == 0 and j == 0:
            return 0, [0]
        if i < 0 or j <= 0:
            return float('inf'), []
        
        # Check memo table
        if memo[i][j] is not None:
            return memo[i][j]
        
        min_cost = float('inf')
        min_path = []
        for p in range(max(0, i - k), i):
            current_cost, current_path = dp(p, j - 1)
            current_cost += platform_costs[p]
            if current_cost < min_cost:
                min_cost = current_cost
                min_path = current_path + [i]

        memo[i][j] = (min_cost, min_path)
        return memo[i][j]

    result = float('inf')
    final_path = []
    for i in range(n):
        if i + k >= n:  # Check if the jump can take you across the river
            current_cost, path = dp(i, m - 1)
            if current_cost < result:
                result = current_cost + platform_costs[i]
                final_path = path  # Do not add 'n' to the path

    return (result, final_path) if result != float('inf') else (-1, [])  # Return -1 if not possible

def main():
    # Reading input from stdin
    first_line = sys.stdin.readline().strip()
    n, k, m = map(int, first_line.split())

    second_line = sys.stdin.readline().strip()
    platform_costs = list(map(int, second_line.split()))

    min_cost, path = min_cost_to_cross_river(n, platform_costs, k, m)
    if min_cost != -1:
        output = ' '.join(map(str, path))
        print(output)
    else:
        print("No valid path found")

if __name__ == "__main__":
    main()
