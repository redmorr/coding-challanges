class Solution:
    def hasPathSum(self, root, sum):
        res = []
        self.dfs(root, sum, res)
        return any(res)

    def dfs(self, node, target, res):
        if node:
            if not node.left and not node.right and node.val == target:
                res.append(True)
            if node.left:
                self.dfs(node.left, target - node.val, res)
            if node.right:
                self.dfs(node.right, target - node.val, res)
