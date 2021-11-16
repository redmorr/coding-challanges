class Solution:
    def longestPalindrome(self, word: str) -> str:
        dp = {}

        # small edge cases
        if len(word) == 1:
            return word

        if len(word) == 2:
            if word[0] == word[1]:
                return word
            else:
                return word[0]

        # init single and double letters
        for i in range(len(word) - 1):
            dp[(i, i)] = word[i]
            if word[i] == word[i+1]:
                dp[(i, i+1)] = word[i] + word[i+1]

        i = len(word) - 1
        dp[(i, i)] = word[i]
        if word[i-1] == word[i]:
            dp[(i-1, i)] = word[i-1] + word[i]

        # print(dp)


        while True:
            new_dp = {}
            for (x, y) in dp.keys():
                if x - 1 >= 0 and y + 1 < len(word) and word[x-1] == word[y+1]:
                    new_dp[(x - 1, y + 1)] = word[x-1] + dp[(x, y)] + word[y+1]
            if len(new_dp) == 0:
                break
            dp = new_dp
            # print(dp)
        return max(dp.values(), key=lambda item: len(item))


