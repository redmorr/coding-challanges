import pytest

import alternative_dfs
import dfs


def grow_tree(list_of_nodes: []):
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    if len(list_of_nodes) == 0:
        return None

    root = TreeNode(list_of_nodes.pop(0))
    queue = [root]

    while list_of_nodes:
        node = queue.pop(0)
        left = list_of_nodes.pop(0)
        right = list_of_nodes.pop(0)
        if left is not None:
            node.left = TreeNode(left)
            queue.append(node.left)
        if right is not None:
            node.right = TreeNode(right)
            queue.append(node.right)

    return root


testcases = [(25, grow_tree([1, 2, 3])),
             (1026, grow_tree([4, 9, 0, 5, 1]))]


@pytest.mark.parametrize('expected, root', testcases)
@pytest.mark.parametrize('solution_class', [dfs.Solution, alternative_dfs.Solution], ids=["DFS", "Alt DFS"])
def test_longest_univalue_path(solution_class, expected, root):
    assert solution_class().sumNumbers(root) == expected
