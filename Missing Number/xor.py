class Solution:
    def missingNumber(self, nums: [int]) -> int:
        s = 0
        for i in nums:
            s = s ^ i
            print(s)
        for i in range(len(nums)):
            s = s ^ i
        s = s ^ (i + 1)
        return s