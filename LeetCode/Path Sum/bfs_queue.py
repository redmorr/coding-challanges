class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        queue = [(root, sum-root.val)]
        while queue:
            node, val = queue.pop(0)
            if not node.left and not node.right and val == 0:
                return True
            if node.left:
                queue.append((node.left, val-node.left.val))
            if node.right:
                queue.append((node.right, val-node.right.val))
        return False