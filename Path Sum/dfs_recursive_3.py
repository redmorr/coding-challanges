class Solution:
    def pathSum(self, root, target_sum):
        if root:
            if root.left is None and root.right is None:
                if root.val == target_sum:
                    return 1
                else:
                    return 0

        self.res = 0
        self.dfs(root, target_sum, [])
        return self.res

    def dfs(self, node, target_sum, cumsums):
        if node:
            new_cumsums = []
            for sum in cumsums:
                sum += node.val
                new_cumsums.append(sum)
                if sum == target_sum:
                    self.res += 1
            if node.val == target_sum:
                self.res += 1
            new_cumsums.append(node.val)
            if node.left:
                self.dfs(node.left, target_sum, new_cumsums)
            if node.right:
                self.dfs(node.right, target_sum, new_cumsums)
