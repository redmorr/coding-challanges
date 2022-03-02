import numpy


def make_square_matrix(n):
    return [[i for i in range(n * j + 1, n * j + n + 1)] for j in range(0, n)]


def show(m):
    print(numpy.array(m))


def rotate(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)

    layer = 0
    while layer < n / 2:
        first = layer
        last = n - 1 - layer
        i = first
        while i < last:
            offset = i - first
            top = matrix[first][i]

            # left-> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom-> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right-> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top-> right
            matrix[i][last] = top  # right <- saved top

            ###
            i += 1

        ###
        layer += 1
    return True


m = make_square_matrix(6)
show(m)
show(numpy.rot90(m, k=-1))
rotate(m)
show(m)
