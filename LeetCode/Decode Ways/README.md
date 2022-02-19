# Decode Ways
https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z can be encoded into numbers using the following mapping:

    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the 
mapping above (there may be multiple ways). For example, "11106" can be mapped into:

    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)

Note that the grouping `(1 11 06)` is invalid because `"06"` cannot be mapped into `'F'` since `"6"` is different from 
`"06"`.

Given a string `s` containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

# Brute force

For every possibility add another path. Algorithm doest work and scales very poorly. At 50 length string it has to be 
terminated for executing too long.

# DFS
https://leetcode.com/problems/decode-ways/discuss/608268/Python-Thinking-process-diagram-(DP-%2B-DFS)

If first 2 digits are less than 26 use recurrence of two paths. If more than 26 return one path of recurrence. Add stop 
conditions. Use `@lru_cache` to heavily reduce execution time by using memoization. Without it if works even worse than
brute force.