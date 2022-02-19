# Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Permutation solution
Check all combinations of `ones` and `twos` and replace 2 `ones` with 1 `two` then check all permutations again

https://brilliant.org/wiki/permutations-with-repetition/
Permutation with all elements distinct: n!
Permutation with 8 elements total, but there are 2 and 3 copies, the 3 remaining are distinct: `8! / 3!2!`

# Fibonacci solution
Solutions of `n0` are solutions of `n-1` (you add `ones`) and solutions of `n-2` (you add `twos`)