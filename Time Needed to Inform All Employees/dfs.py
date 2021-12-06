class Solution:
    def numOfMinutes(self, n, head_id, manager, inform_time):
        def dfs(i):
            if manager[i] != -1:
                inform_time[i] += dfs(manager[i])
                manager[i] = -1
            return inform_time[i]
        return max(map(dfs, range(n)))
