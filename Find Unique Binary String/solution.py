class Solution:
    def findDifferentBinaryString(self, nums: [str]) -> str:
        res = ''

        for i, number in enumerate(nums):
            res += '1' if number[i] == '0' else '0'
        return res
