class Solution(object):
    def pathSum(self, root, target):
        self.result = 0
        cache = {0: 1}
        self.dfs(root, target, 0, cache)
        return self.result

    def dfs(self, root, target, curr_path, cache):
        if root is None:
            return

        curr_path += root.val
        old_path = curr_path - target
        self.result += cache.get(old_path, 0)
        cache[curr_path] = cache.get(curr_path, 0) + 1

        self.dfs(root.left, target, curr_path, cache)
        self.dfs(root.right, target, curr_path, cache)
        cache[curr_path] -= 1
