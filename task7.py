class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [float('inf')] * (4 * n)

    def update(self, idx, val, node=1, node_left=0, node_right=None):
        if node_right is None:
            node_right = self.n - 1

        if node_left == node_right:
            self.tree[node] = val
            return

        mid = (node_left + node_right) // 2
        if idx <= mid:
            self.update(idx, val, 2 * node, node_left, mid)
        else:
            self.update(idx, val, 2 * node + 1, mid + 1, node_right)

        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, l, r, node=1, node_left=0, node_right=None):
        if node_right is None:
            node_right = self.n - 1

        if l > node_right or r < node_left:
            return float('inf')

        if l <= node_left and r >= node_right:
            return self.tree[node]

        mid = (node_left + node_right) // 2
        left_min = self.query(l, r, 2 * node, node_left, mid)
        right_min = self.query(l, r, 2 * node + 1, mid + 1, node_right)
        return min(left_min, right_min)

# Now we will implement the dynamic programming logic using this segment tree.


def find_optimal_path_with_segment_tree(n, m, k, cost):
    # Initialize Segment Trees for each jump count
    trees = [SegmentTree(n) for _ in range(m)]
    dp_path = [[[] for _ in range(m)] for _ in range(n)]

    # Initial platform cost and path
    trees[0].update(0, cost[0])
    dp_path[0][0] = [0]

    # Fill DP tables using Segment Trees
    for i in range(1, n):
        for j in range(1, min(i + 1, m)):
            # Query the segment tree for the minimum cost within jump range
            left = max(0, i - k)
            right = i - 1
            min_cost = trees[j - 1].query(left, right)

            if min_cost != float('inf'):
                new_cost = min_cost + cost[i]
                trees[j].update(i, new_cost)

                # Find the platform from where this min cost was achieved
                for p in range(left, right + 1):
                    if dp_path[p][j - 1] and trees[j - 1].query(p, p) == min_cost:
                        dp_path[i][j] = dp_path[p][j - 1] + [i]
                        break

    # Ensure the path uses exactly m-1 jumps to reach the last platform
    if dp_path[-1][m - 1]:
        return dp_path[-1][m - 1]
    else:
        return "No path found"


"""n = 8
k = 4
m = 4
cost = [12, 5, 8, 9, 11, 13, 16, 1]
"""


n = 8
k = 3
m = 4
cost = [8, 9, 6, 3, 2, 5, 4, 1]

# Test the function with the given parameters
result = find_optimal_path_with_segment_tree(n, m, k, cost)
print(result)

# Example usage


