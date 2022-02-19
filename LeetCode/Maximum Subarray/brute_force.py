class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        sums = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sums.append(sum(nums[i:j+1]))
        return max(sums)


# s = Solution()
# print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
