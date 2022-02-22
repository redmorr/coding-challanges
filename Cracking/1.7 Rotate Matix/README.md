# 1.7 Rotate Matix

Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the
image by 90 degrees. Can you do this in place?

# Sources

https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python

# Comments

`map(list, (zip(*m))` is used to because of `zip` returning tuples instead of lists. This conversion is probably
inefficient.