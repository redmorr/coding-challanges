class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        tortoise, hare, check = 0, 0, 0
        print()
        while True:
            print(nums[tortoise], nums[nums[hare]])
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        print()
        while True:
            print( nums[tortoise], nums[check])
            tortoise = nums[tortoise]
            check = nums[check]
            if tortoise == check:
                break

        return check
