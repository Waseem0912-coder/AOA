import sys

class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [float('inf')] * (2 * size)
        self.index_tree = [None] * (2 * size)

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
    paths = [[] for _ in range(n)]
    paths[0] = [0]

    for i in range(1, n):
        start = max(0, i - k)
        min_cost_in_range, prev_index = segment_tree.query(start, i)
        min_costs[i] = min_cost_in_range + cost[i]
        paths[i] = paths[prev_index] + [i]
        segment_tree.update(i, min_costs[i])

    return min_costs[-1], paths[-1]

# Reading input from stdin
first_line = sys.stdin.readline().strip()
n, k = map(int, first_line.split())

second_line = sys.stdin.readline().strip()
cost = list(map(int, second_line.split()))

min_cost_revised, path_revised = minCostDPWithSegmentTreeRevised(cost, k)

# Formatting output
output = ' '.join(map(str, path_revised))
print(output)
