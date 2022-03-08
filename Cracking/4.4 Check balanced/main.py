from __future__ import annotations
from plot import plot_binary_tree
from node import Node

unbalanced_binary_tree = Node(0, left=Node(1,
                                           left=Node(3,
                                                     left=Node(7,
                                                               left=Node(9),
                                                               right=Node(10)),
                                                     right=Node(8)),
                                           right=Node(4)),
                              right=Node(2,
                                         left=Node(5),
                                         right=Node(6)))

balanced_binary_tree = Node(0, left=Node(1,
                                         left=Node(3,
                                                   left=Node(7),
                                                   right=Node(8)),
                                         right=Node(4)),
                            right=Node(2,
                                       left=Node(5),
                                       right=Node(6)))


def get_height(node):
    lh, rh = 0, 0

    if node.left:
        lh = get_height(node.left)
        if lh == -1:
            return -1
    if node.right:
        rh = get_height(node.right)
        if rh == -1:
            return -1

    if abs(lh - rh) > 1:
        return -1
    else:
        return max(lh, rh) + 1


def is_balanced(node):
    return get_height(node) != -1


plot_binary_tree(unbalanced_binary_tree)
plot_binary_tree(balanced_binary_tree)

print(is_balanced(unbalanced_binary_tree))
print(is_balanced(balanced_binary_tree))
