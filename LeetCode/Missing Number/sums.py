class Solution:
    def missingNumber(self, nums: [int]) -> int:
        # return sum(range(len(nums) + 1)) - sum(nums)
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
