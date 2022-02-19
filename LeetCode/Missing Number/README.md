# Missing Number
https://leetcode.com/problems/missing-number/

Similar: `Single Number`, `Find the Duplicate Number`, `Find Unique Binary String`, `Couples Holding Hands`

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

**Example 1:**

    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

**Example 2:**

    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

**Example 3:**

    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

**Example 4:**

    Input: nums = [0]
    Output: 1
    Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.

**Constraints:**

    n == nums.length
    1 <= n <= 10^4
    0 <= nums[i] <= n
    All the numbers of nums are unique.


## Solution 1 - Iterate and check
CHeck if every number from `0` is in the list. It's quite slow.

## Solution 2 - Subtract sums
Subtract sum of series `1 + 2 + ... + (n - 1 + n)` where `n `is the of length of the `nums` from a sum of the `nums` to 
get the result. Notice that the series form above can be calculater for the formula:

`1 + 2 + ... + (n - 1 + n) = n * (n + 1) / 2`

## Solution 3 - XOR
Property of XOR:

    2 ^ 2 = 0,
    1 ^ 1 ^ 2 ^ 2 = 0,
    a ^ a ^ b ^ b ^ c ^ c = (a ^ a) ^ (b ^ b) ^ (c ^ c) = 0 ^ 0 ^ 0 = 0

Basically what it means is that doing `XOR` on two of the same numbers yields `0` no matter the order.

Given nums [0, 3, 1]:

`(0 ^ 3 ^ 1) ^ (0 ^ 1 ^ 2 ^ 3) = 2`

All numbers repeated even number of times will cancel out leaving only odd numbers. In this puzzle all numbers are 
unique and doing XOR with series which contains one more number will make this number stand out.