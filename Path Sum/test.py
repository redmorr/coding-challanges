import pytest

from treenode import TreeNode
import dfs_recursive
import dfs_stack
import bfs_queue


def grow_tree(list_of_nodes):
    if len(list_of_nodes) == 0:
        return None

    root = TreeNode(list_of_nodes[0])
    layer = [root]
    count = 1

    while count < len(list_of_nodes):
        new_layer = []
        for node in layer:
            left = list_of_nodes[count:][0]
            right = list_of_nodes[count:][1]
            if left is not None:
                node.left = TreeNode(left)
                new_layer.append(node.left)
            if right is not None:
                node.right = TreeNode(right)
                new_layer.append(node.right)
            count += 2
        layer = new_layer

    return root


testcases = [(True, 22, grow_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])),
             (False, 5, grow_tree([1, 2, 3])),
             (False, 0, grow_tree([]))]

testcases2 = [([[5, 4, 11, 2], [5, 8, 4, 5]], 22, grow_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])),
              ([], 5, grow_tree([1, 2, 3])),
              ([], 0, grow_tree([]))]


@pytest.mark.parametrize('expected, target_sum, root', testcases)
@pytest.mark.parametrize('solution_class', [dfs_recursive.Solution, dfs_stack.Solution, bfs_queue.Solution],
                         ids=['DFS Recursive', 'DFS Stack', 'BFS Queue'])
def test_has_path_sum(solution_class, expected, target_sum, root):
    assert solution_class().hasPathSum(root, target_sum) == expected


@pytest.mark.parametrize('expected, target_sum, root', testcases2)
@pytest.mark.parametrize('solution_class', [dfs_recursive.Solution], ids=['DFS Recursive'])
def test_has_path_sum_2(solution_class, expected, target_sum, root):
    result = solution_class().pathSum(root, target_sum)
    for i, row in enumerate(expected):
        for j, _ in enumerate(row):
            assert expected[i][j] == result[i][j]
