class Solution:
    def generate(self, numRows: int) -> [[int]]:
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        triangle = [[1], [1, 1]]

        if numRows == 2:
            return triangle

        for i in range(3, numRows + 1):
            new_layer = [1]
            for index in range(0, i-2):
                new_layer.append(triangle[-1][index] + triangle[-1][index + 1])
            new_layer.append(1)
            triangle.append(new_layer)
        return triangle

    def getRow(self, n: int) -> [int]:
        if n == 0:
            return [1]

        if n == 1:
            return [1, 1]

        if n == 2:
            return [1, 2, 1]

        if n == 3:
            return [1, 3, 3, 1]

        row = [1, n]
        middle = n // 2 + 1
        for i in range(2, middle):
            res = row[-1] * (n - i + 1) // i
            row.append(res)

        if n % 2 == 0:
            return row + row[-2::-1]
        else:
            return row + row[::-1]


s = Solution()

n = 9
print(s.generate(n+1))
print(s.getRow(n))
n = 10
print(s.generate(n+1))
print(s.getRow(n))
