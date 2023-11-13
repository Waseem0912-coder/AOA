import sys

def min_cost_bottom_up(n, k, m, cost):
    # Initialize DP table with infinity
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    # Store the path
    path = [[[] for _ in range(m + 1)] for _ in range(n + 1)]

    for jumps in range(1, m + 1):
        for platform in range(n):
            for jump in range(1, k + 1):
                if platform + jump <= n:
                    next_cost = dp[platform][jumps - 1] + cost[platform]
                    if next_cost < dp[platform + jump][jumps]:
                        dp[platform + jump][jumps] = next_cost
                        path[platform + jump][jumps] = path[platform][jumps - 1] + [platform]

    # Reconstruct the path
    min_cost_path = path[n][m] if dp[n][m] != float('inf') else []
    return min_cost_path

def main():
    # Reading input from stdin
    first_line = sys.stdin.readline().strip()
    n, k, m = map(int, first_line.split())

    second_line = sys.stdin.readline().strip()
    cost = list(map(int, second_line.split()))

    min_cost_path = min_cost_bottom_up(n, k, m, cost)
    if min_cost_path:
        output = ' '.join(map(str, min_cost_path))
        print(output)
    else:
        print("No valid path found")

if __name__ == "__main__":
    main()
