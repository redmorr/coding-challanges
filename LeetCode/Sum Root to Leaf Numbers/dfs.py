class Solution:
    def sumNumbers(self, root):
        self.sum = 0
        self.dfs(root, 0)
        return self.sum

    def dfs(self, node, number):
        a = number * 10 + node.val
        if node.left:
            self.dfs(node.left, a)
        if node.right:
            self.dfs(node.right, a)
        if not node.left and not node.right:
            self.sum += a