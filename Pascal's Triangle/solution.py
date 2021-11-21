class Solution:
    def generate(self, numRows: int) -> [[int]]:
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
        print(triangle)
        return triangle


s = Solution()
s.generate(30)
