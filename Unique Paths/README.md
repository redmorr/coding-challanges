# Unique Path's I
A robot is located at the top-left corner of a `m x n` grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner 
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

**Example 1:**

| S | . | . | . | . | . | . |
|---|---|---|---|---|---|---|
| . | . | . | . | . | . | . |
| . | . | . | . | . | . | F |

S = Start

F = Finish

    Input: m = 3, n = 7
    Output: 28

**Example 2:**

    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down

**Example 3:**

    Input: m = 7, n = 3
    Output: 28

**Example 4:**

    Input: m = 3, n = 3
    Output: 6

**Constraints:**

    1 <= m, n <= 100
    It's guaranteed that the answer will be less than or equal to 2 * 10^9.

# Solution 1 - Recursion
Pass next possible grid coord to the function until a wall is met then return `1`, which means an unique path has been 
discovered. The number of recursion calls is a number of all unique paths. Reduce computation time by adding memoization 
as the function is called with the same arguments multiple times.

# Solution 2 - DP
https://leetcode.com/problems/unique-paths/discuss/22954/C%2B%2B-DP

Initialize the grid with ones. Iterate through the grid adding cells from the left and above which means that the path 
the current cell is a sum of paths from above and the left. 

    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

| 1 | 1 | 1 | 1 | 1 | 1 | 1 |
|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 1 | 3 | 6 | 10| 15| 21| 28|

Optimize the memory use by using only one list and reusing previous result which corrsepond with a row above in the 
completed grid.

    dp[j] = dp[j] + dp[j - 1]

| 1 | 1 | 1 | 1 | 1 | 1 | 1 |
|---|---|---|---|---|---|---|

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|

| 1 | 3 | 6 | 10| 15| 21| 28|
|---|---|---|---|---|---|---|


# Solution 3 - Combination
https://leetcode.com/problems/unique-paths/discuss/22958/Math-solution-O(1)-space

All possible paths are the combination of going `DOWN` or `RIGHT` until we are in the right bottom corner.
To achieve the goal in a `3 x 7` grid we have to make the following moves in any order: `R R R R R R D D`. 
So basically 6 times `R` and 2 times `D`. 

    C(m+n,n) or C(m+n,m) where m and n are substracted by 1
    C(8,2) = 8! / (6! * 2!) or 
    C(8,6) = 8! / (2! * 6!)

Avoid calulating large factorials by using iteration with decreasing multiplication by 1 and increasing division by 1.

# Unique Path's II 
https://leetcode.com/problems/unique-paths-ii/

A robot is located at the top-left corner of a `m x n` grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner 
of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as `1` and `0` respectively in the grid.

**Example 1:**

| S | . | . |
|---|---|---|
| . | O | . |
| . | . | F |

S = Start

F = Finish

O = Obstacle

    Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2
    Explanation: There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right

**Constraints:**

    m == obstacleGrid.length
    n == obstacleGrid[i].length
    1 <= m, n <= 100
    obstacleGrid[i][j] is 0 or 1.

# Solution 1 - Recursion
Reuse previous recursive solution with more conditions added:
* return 0 if helper met an obstacle, it means this is nota valid path
* if a wall is met continue along with it to check for obstacles instead of assuming there is only one valid path

# Solution 2 - DP
Anything after an obstacle in the first row is inaccessible so all possible paths after that are 0. After initializing 
first row reuse DP solution from Unique Path's I, but whenever there is an obstacle inset zero.

