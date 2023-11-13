import sys

def min_cost_brute_force(n, k, m, cost):
    def explore(platform, jumps_remaining, path):
        if jumps_remaining == 0:
            return (0, path) if platform >= n else (float('inf'), [])
        if platform >= n:
            return (float('inf'), [])

        min_cost = float('inf')
        min_path = []
        for jump in range(1, k + 1):
            next_platform = platform + jump
            if next_platform < n:
                jump_cost = cost[next_platform]
            else:
                jump_cost = 0  # No cost if jumping to the other side of the river

            current_cost, current_path = explore(next_platform, jumps_remaining - 1, path + [platform])
            current_cost += jump_cost

            if current_cost < min_cost:
                min_cost = current_cost
                min_path = current_path

        return min_cost, min_path

    min_cost, min_path = explore(0, m, [])
    return min_path

def main():
    # Reading input from stdin
    first_line = sys.stdin.readline().strip()
    n, k, m = map(int, first_line.split())

    second_line = sys.stdin.readline().strip()
    cost = list(map(int, second_line.split()))

    min_path = min_cost_brute_force(n, k, m, cost)

    # Formatting output
    output = ' '.join(map(str, min_path))
    print(output)

if __name__ == "__main__":
    main()
