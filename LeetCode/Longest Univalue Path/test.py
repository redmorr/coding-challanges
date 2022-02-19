import pytest
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
        if left:
            node.left = TreeNode(left)
            queue.append(node.left)
        if right:
            node.right = TreeNode(right)
            queue.append(node.right)

    return root


testcases = [(2, grow_tree([5, 4, 5, 1, 1, None, 5])),
             (2, grow_tree([1, 4, 5, 4, 4, None, 5]))]


@pytest.mark.parametrize('expected, root', testcases)
def test_longest_univalue_path(expected, root):
    assert dfs.Solution().longestUnivaluePath(root) == expected
