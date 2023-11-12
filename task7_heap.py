import heapq

def find_optimal_path_with_priority_queue(n, m, k, cost):
    # Initialize priority queues for each jump count
    pq = [[] for _ in range(m)]
    dp_path = [[[] for _ in range(m)] for _ in range(n)]

    # Initial platform cost and path
    heapq.heappush(pq[0], (cost[0], 0))
    dp_path[0][0] = [0]

    # Process each jump count
    for j in range(1, m):
        for prev_platform in range(n):
            # Skip if there's no path to prev_platform with j-1 jumps
            if not dp_path[prev_platform][j-1]:
                continue

            prev_cost = sum(cost[i] for i in dp_path[prev_platform][j-1])

            # Explore jumps from prev_platform to next platforms within range
            for next_platform in range(prev_platform + 1, min(prev_platform + k + 1, n)):
                new_cost = prev_cost + cost[next_platform]

                # Update if new path is cheaper or not set
                if not dp_path[next_platform][j] or new_cost < sum(cost[i] for i in dp_path[next_platform][j]):
                    dp_path[next_platform][j] = dp_path[prev_platform][j-1] + [next_platform]

    # Ensure the path uses exactly m-1 jumps to reach the last platform
    if dp_path[-1][m - 1]:
        return dp_path[-1][m - 1]
    else:
        return "No path found"

# Test the function with the given parameters
n= 8
k = 3
m = 5
cost = [8, 9, 6, 3, 2, 5, 4, 1]

result = find_optimal_path_with_priority_queue(n, m, k, cost)
print(result)


