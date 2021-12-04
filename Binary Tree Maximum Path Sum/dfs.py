class Solution:
    def maxPathSum(self, root):
        self.max_path = -1001
        self.dfs(root)
        return self.max_path

    def dfs(self, node):
        if not node:
            return 0

        left_path = self.dfs(node.left)
        right_path = self.dfs(node.right)
        self.max_path = max(self.max_path, left_path + right_path + node.val)
        return max(left_path + node.val, right_path + node.val, node.val, 0)
