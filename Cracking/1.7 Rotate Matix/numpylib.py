import numpy

m = numpy.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]], int)

print(m)

print(numpy.rot90(m))  # once left
print(numpy.rot90(m, k=2))  # twice left
print(numpy.rot90(m, k=3))  # thrice left
print(numpy.rot90(m, k=4))  # four times left

print()
print(m)

print(numpy.rot90(m, k=-1))  # once right
print(numpy.rot90(m, k=-2))  # twice right
print(numpy.rot90(m, k=-3))  # thrice right
print(numpy.rot90(m, k=-4))  # four times right
