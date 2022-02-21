# 1.6 String Compression

Implement a method to perform basic string compression using the counts of repeated characters. If the "compressed"
string would not become smaller than the original string, your method should return the original string You can assume
the string has only uppercase and lowercase letters (a - z).

**Example:**

aabcccccaaa ->  a2blc5a3

**Solutions:**

1. Count letters, store them in a list, **efficiently** concatenate at the end

# Comments

### Use `str.join()` once at the end instead the `+`

https://python.plainenglish.io/concatenating-strings-efficiently-in-python-9bfc8e8d6f6e

Concatenating immutable sequences always results in a new object. This means that building up a sequence by repeated
concatenation will have a **quadratic** runtime cost in the total sequence length.

Concatenating strings with `+` is a costly operation especially if string to be concatenated is long

If we observe the pattern, the number of copies during concatenation
is `1(no of characters) + 2(number of characters) + 3(number of characters) + ….. + (n)` .

This gets us to the sum of n natural numbers which is `n(n+1)/2` which will give us `O(xn²)`, where `x` = number of
characters. Since the number of characters for every concatenation is always constant here(1 in this case) we could drop
the constant factor which gives us `O(n²)`.
