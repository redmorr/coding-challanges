class Solution:
    def missingNumber(self, nums: [int]) -> int:
        i = 0
        while i in nums:
            i += 1
        return i