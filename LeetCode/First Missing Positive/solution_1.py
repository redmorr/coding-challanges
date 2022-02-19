class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        return min({x for x in range(1, len(nums) + 2)} - {x for x in nums if x >= 1})
