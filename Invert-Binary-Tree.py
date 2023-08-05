# https://leetcode.com/problems/invert-binary-tree/

from collections import defaultdict


class Solution:
    nodes = defaultdict(list)
    vals = defaultdict(list)

    def bfs(self, root, b):
        if root:
            if b % 2 == 1:
                self.nodes[b].append(root)
                self.vals[b].append(root.val)
            self.bfs(root.left, b + 1)
            self.bfs(root.right, b + 1)

    def reverseOddLevels(self, root):
        self.nodes = []
        self.vals = []
        self.bfs(root, 0)
        for i in self.nodes:
            for j in range(len(self.nodes[i])):
                self.nodes[i][j].val = self.vals[i][j]
        return root