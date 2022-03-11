from __future__ import annotations
from plot import plot_binary_tree
from node import Node

tree = Node(0,
            left=Node(1,
                      left=Node(3)),
            right=Node(2,
                       right=Node(4,
                                  left=Node(5),
                                  right=Node(6))))

sub_tree = Node(4,
                left=Node(5),
                right=Node(6))


# plot_binary_tree(binary_tree)


def in_order(node):
    if node.left:
        in_order(node.left)


    if node.right:
        in_order(node.right)
    print(node)


in_order(tree)
print()
in_order(sub_tree)
