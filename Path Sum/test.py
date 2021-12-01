import pytest

from treenode import TreeNode
import dfs_recursive_1
import dfs_recursive_2
# import dfs_recursive_3
import dfs_stack
import bfs_queue


def grow_tree(list_of_nodes: []):
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


testcases = [(True, 22, grow_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])),
             (False, 5, grow_tree([1, 2, 3])),
             (False, 0, grow_tree([]))]

testcases2 = [([[5, 4, 11, 2], [5, 8, 4, 5]], 22, grow_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])),
              ([], 5, grow_tree([1, 2, 3])),
              ([], 0, grow_tree([]))]

testcases3 = [(3, 8, grow_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]))]


@pytest.mark.parametrize('expected, target_sum, root', testcases)
@pytest.mark.parametrize('solution_class', [dfs_recursive_1.Solution, dfs_stack.Solution, bfs_queue.Solution],
                         ids=['DFS Recursive', 'DFS Stack', 'BFS Queue'])
def test_path_sum_1(solution_class, expected, target_sum, root):
    assert solution_class().hasPathSum(root, target_sum) == expected


@pytest.mark.parametrize('expected, target_sum, root', testcases2)
@pytest.mark.parametrize('solution_class', [dfs_recursive_2.Solution], ids=['DFS Recursive'])
def test_path_sum_2(solution_class, expected, target_sum, root):
    result = solution_class().pathSum(root, target_sum)
    for i, row in enumerate(expected):
        for j, _ in enumerate(row):
            assert expected[i][j] == result[i][j]
#
#
# @pytest.mark.parametrize('expected, target_sum, root', testcases3)
# @pytest.mark.parametrize('solution_class', [dfs_recursive_3.Solution], ids=['DFS Recursive'])
# def test_path_sum_3(solution_class, expected, target_sum, root):
#     assert solution_class().pathSum(root, target_sum) == expected
