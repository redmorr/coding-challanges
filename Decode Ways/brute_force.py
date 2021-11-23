class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            if s[0] == '0':
                return 0
            return 1

        if s[0] == '0':
            return 0

        dp = [[int(s[0])]]

        for digit in s[1:]:
            new_dp = []
            for path in dp:
                if int(digit) != 0:
                    new_dp.append(path + [int(digit)])
                if path[-1] * 10 + int(digit) <= 26:
                    new_dp.append(path[:-1] + [path[-1] * 10 + int(digit)])
            # print(new_dp)
            dp = new_dp
            # print("Current possible paths: " + str(len(dp)))
        return len(dp)
