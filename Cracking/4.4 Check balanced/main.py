from __future__ import annotations
from plot import plot_binary_tree
from node import Node

binary_tree = Node(0, left=Node(1,
                                left=Node(3,
                                          left=Node(7,
                                                    left=Node(9),
                                                    right=Node(10)),
                                          right=Node(8)),
                                right=Node(4)),
                   right=Node(2,
                              left=Node(5),
                              right=Node(6)))

plot_binary_tree(binary_tree)


def get_height(node):
    lh, rh = 0, 0

    if node.left:
        lh = get_height(node.left)
    if node.right:
        rh = get_height(node.right)

    return max(lh, rh) + 1


print(get_height(binary_tree))
