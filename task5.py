def find_min_cost_jump(n, k, cost, m):
    min_cost = float('inf')
    min_cost_sequence = []

    def recurse(current, jumps, total_cost, jump_count):
        nonlocal min_cost, min_cost_sequence
        if jump_count == m:
            if current == n - 1 and total_cost < min_cost:
                min_cost = total_cost
                min_cost_sequence = jumps.copy()
            return

        if jump_count > m or current == n - 1:
            return

        for i in range(1, k + 1):
            if current + i < n:
                new_jump = current + i
                jumps.append(new_jump)
                recurse(new_jump, jumps, total_cost + cost[new_jump], jump_count + 1)
                jumps.pop()

    recurse(0, [0], cost[0], 1)
    return min_cost_sequence, min_cost

# Input
n = 8
k = 4
cost = [12, 5, 8, 9, 11, 13, 16, 1]
m = 4

# Output
min_cost_jump_indices, min_cost = find_min_cost_jump(n, k, cost, m)

# Print the minimum cost and the sequence of jumps
print(f"Minimum Cost: {min_cost}")
print("Jump Sequence:")
for index in min_cost_jump_indices:
    print(index)
