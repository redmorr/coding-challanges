class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            node, val = stack.pop()
            if not node.left and not node.right and val == sum:
                return True
            if node.left:
                stack.append((node.left, val + node.left.val))
            if node.right:
                stack.append((node.right, val + node.right.val))
        return False
