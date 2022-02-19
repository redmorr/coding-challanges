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


testcases = [(6, grow_tree([1, 2, 3])),
             (42, grow_tree([-10, 9, 20, None, None, 15, 7])),
             (2, grow_tree([2, -1, None])),
             (-3, grow_tree([-3])),
             (2, grow_tree([2, -1, -2]))]


@pytest.mark.parametrize('expected, root', testcases)
def test_longest_univalue_path(expected, root):
    assert dfs.Solution().maxPathSum(root) == expected
