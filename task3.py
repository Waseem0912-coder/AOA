
class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [float('inf')] * (2 * size)
        self.index_tree = [None] * (2 * size)  # Additional tree to store indices

    def update(self, index, value):
        idx = index
        index += self.size
        self.tree[index] = value
        self.index_tree[index] = idx
        while index > 1:
            index //= 2
            left = self.tree[2 * index]
            right = self.tree[2 * index + 1]
            if left < right:
                self.tree[index] = left
                self.index_tree[index] = self.index_tree[2 * index]
            else:
                self.tree[index] = right
                self.index_tree[index] = self.index_tree[2 * index + 1]

    def query(self, left, right):
        min_val = float('inf')
        min_index = None
        left += self.size
        right += self.size
        while left < right:
            if left % 2:
                if self.tree[left] < min_val:
                    min_val = self.tree[left]
                    min_index = self.index_tree[left]
                left += 1
            if right % 2:
                right -= 1
                if self.tree[right] < min_val:
                    min_val = self.tree[right]
                    min_index = self.index_tree[right]
            left //= 2
            right //= 2
        return min_val, min_index

def minCostDPWithSegmentTreeRevised(cost, k):
    n = len(cost)
    segment_tree = SegmentTree(n)
    segment_tree.update(0, cost[0])

    min_costs = [float('inf')] * n
    min_costs[0] = cost[0]
    paths = [[] for _ in range(n)]  # Initialize paths
    paths[0] = [0]

    for i in range(1, n):
        start = max(0, i - k)
        min_cost_in_range, prev_index = segment_tree.query(start, i)
        min_costs[i] = min_cost_in_range + cost[i]
        paths[i] = paths[prev_index] + [i]
        segment_tree.update(i, min_costs[i])

    return min_costs[-1], paths[-1]

# Calculate the minimum cost and path with the revised approach
n = 8  # Number of platforms
k = 4   # Maximum jump length
cost = [12, 5, 8, 9, 11, 13, 16, 1]  # Given cost for each platform

min_cost_revised, path_revised = minCostDPWithSegmentTreeRevised(cost, k)
print("Minimum Cost:", min_cost_revised)
print("Path:", path_revised)
