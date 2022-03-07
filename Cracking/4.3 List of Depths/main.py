from __future__ import annotations
from plot import plot_binary_tree
from node import Node

binary_tree = Node(1, left=Node(2,
                                left=Node(4),
                                right=Node(5)),
                   right=Node(3,
                              left=Node(6),
                              right=Node(7)))

plot_binary_tree(binary_tree)


def dfs(root):
    def helper(node, hash_table: {}, i):
        layer = hash_table.get(i, [])
        hash_table[i] = layer + [node]
        if node.left:
            helper(node.left, hash_table, i + 1)
        if node.right:
            helper(node.right, hash_table, i + 1)

    node_layers = {}
    helper(root, node_layers, 0)
    return node_layers


print(dfs(binary_tree))  # All is left to do is to link it together
