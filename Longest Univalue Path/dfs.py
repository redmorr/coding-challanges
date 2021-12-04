class Solution:
    def longestUnivaluePath(self, root):
        self.longest = 0
        self.dfs(root)
        return self.longest

    def dfs(self, node):
        if not node:
            return 0

        left_length, right_length = self.dfs(node.left), self.dfs(node.right)
        left = left_length + 1 if node.left and node.left.val == node.val else 0
        right = right_length + 1 if node.right and node.right.val == node.val else 0
        self.longest = max(self.longest, left + right)
        return max(left, right)
