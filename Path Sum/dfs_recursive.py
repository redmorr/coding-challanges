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

    def pathSum(self, root, sum):
        res = []
        self.dfs_2(root, sum, res, [])
        return res

    def dfs_2(self, node, target, res, path):
        if node:
            if not node.left and not node.right and node.val == target:
                res.append(path[:] + [node.val])
            if node.left:
                self.dfs_2(node.left, target - node.val, res, path[:] + [node.val])
            if node.right:
                self.dfs_2(node.right, target - node.val, res, path[:] + [node.val])
