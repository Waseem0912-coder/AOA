def brute_force_min_cost_paths(cost, k, current_platform, depth):
    n = len(cost)
    if depth == n:
        return (0, [[]]) if current_platform >= n else (float('inf'), [])

    min_cost = float('inf')
    unique_paths = set()
    paths_with_min_cost = []
    for jump in range(1, k + 1):
        next_platform = current_platform + jump
        cost_to_next, paths = brute_force_min_cost_paths(cost, k, next_platform, depth + 1)

        if current_platform < n:
            cost_to_next += cost[current_platform]
            new_paths = [tuple(path + [current_platform]) for path in paths]
        else:
            new_paths = [tuple(path) for path in paths]

        if cost_to_next < min_cost:
            min_cost = cost_to_next
            unique_paths = set(new_paths)
        elif cost_to_next == min_cost:
            unique_paths.update(new_paths)

    paths_with_min_cost = [list(path) for path in unique_paths]
    return min_cost, paths_with_min_cost

n = 8
k = 3 
cost = [8, 9, 6, 3, 2, 5, 4, 1]

min_cost, paths = brute_force_min_cost_paths(cost, k, 0, 0)
print('Minimum cost:', min_cost)
print('Path with minimum cost:', ', '.join(map(str, paths[0][::-1])))
