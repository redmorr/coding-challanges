class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        if 1 not in nums: return 1
        if len(nums) == 1: return 2

        n = set(nums)
        i = 1

        while i in n:
            i += 1

        return i