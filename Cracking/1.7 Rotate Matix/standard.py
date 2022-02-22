def show(m):
    for i in m:
        print(i)
    print()


def rotate_90_right(m):
    return list(map(list, (zip(*m[::-1]))))


def rotate_90_left(m):
    return list(reversed(list(map(list, (zip(*m))))))


def flip_diagonally(m):
    return list(map(list, (zip(*m))))


m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

show(m)

m = rotate_90_left(m)
show(m)

m = rotate_90_left(m)
show(m)

m = rotate_90_left(m)
show(m)

m = rotate_90_left(m)
show(m)
