# Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and
return its *sum*.

A **subarray** is a **contiguous** part of an array.

**Example 1:**

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

**Example 2:**

    Input: nums = [1]
    Output: 1

**Example 3:**

    Input: nums = [5,4,-1,7,8]
    Output: 23

**Constraints:**

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4

# Solution 1 - Brute Force
Create every possible subarray and look for the maximum sum. It scales horribly. Results in Time Limit Exceeded

# Solution 2 - Kadane’s Algorithm:
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

The simple idea of Kadane’s algorithm is to look for all positive contiguous segments of the array (`max_ending_here` is 
used for this). And keep track of maximum sum contiguous segment among all positive segments (max_so_far is used for 
this). Each time we get a positive-sum compare it with `max_so_far` and update `max_so_far` if it is greater than 
`max_so_far`

# Solution 3 - ?

# Bonus
### How to load large variables from file instead using literals
```python3
from numpy import loadtxt
large_int_array = loadtxt('large_data.txt', dtype='int', delimiter=',')
```
Or just use another .py file with also long but proper python code

### Grouping tests in pytest: Classes vs plain functions
https://stackoverflow.com/questions/50016862/grouping-tests-in-pytest-classes-vs-plain-functions