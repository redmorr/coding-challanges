from treenode import TreeNode


class Solution:

    def hasPathSum(self, root: [TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def dfs(node, path):
            if path + node.val == targetSum and node.left is None and node.right is None:
                raise Exception
            if node.left is not None:
                dfs(node.left, path + node.val)
            if node.right is not None:
                dfs(node.right, path + node.val)

        try:
            dfs(root, 0)
        except Exception:
            return True

        return False
