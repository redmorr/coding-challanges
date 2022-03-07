class Node:
    __next_id = 1

    def __init__(self, val, left=None, right=None):
        self.id = str(Node.__next_id)
        Node.__next_id += 1
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "n" + str(self.val)

    def __repr__(self):
        return "n" + str(self.val)

    def bfs(self):
        queue = [self]
        while queue:
            node = queue.pop(0)
            print(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs(self):
        def helper(node, hash_table: {}, i):
            layer = hash_table.get(i, [])
            hash_table[i] = layer + [node]
            if node.left:
                helper(node.left, hash_table, i + 1)
            if node.right:
                helper(node.right, hash_table, i + 1)

        node_layers = {}
        helper(self, node_layers, 0)
        return node_layers
