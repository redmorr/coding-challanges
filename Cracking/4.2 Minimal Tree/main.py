from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    val: int
    left: Node
    right: Node


def make_minimal_tree(array):
    print(array)

    if not array:
        return None
    if len(array) == 1:
        return Node(array[0], None, None)

    mid = len(array) // 2 + len(array) % 2 - 1
    return Node(array[mid], make_minimal_tree(array[0:mid]), make_minimal_tree(array[mid + 1:]))


sorted_array = [1, 2, 3, 4, 5, 6, 7, 8]
x = make_minimal_tree(sorted_array)
print(x)
