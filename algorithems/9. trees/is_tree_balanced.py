'''
is_tree_balanced.py
'''
from collections import deque


class TreeNode:
    ''''Binary node definition'''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(arr):
    '''convery array to node'''
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        # Left child
        if i < len(arr):
            if arr[i] is not None:
                node.left = TreeNode(arr[i])
                queue.append(node.left)
            i += 1

        # Right child
        if i < len(arr):
            if arr[i] is not None:
                node.right = TreeNode(arr[i])
                queue.append(node.right)
            i += 1


    return root


def is_balanced(root: TreeNode | None) -> bool:
    """
    Returns True if binary tree is height-balanced.
    Uses -1 to propagate "unbalanced" state upward.
    """
    def dfs(node: TreeNode | None) -> int:
        '''Base case: empty tree has height 0'''
        if not node:
            return 0

        left = dfs(node.left)
        if left == -1:
            return -1

        right = dfs(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return dfs(root) != -1



if __name__ == "__main__":
    # Example 1: Balanced
    root1 = list_to_tree([3, 9, 20, None, None, 15, 7])
    print(is_balanced(root1))  # True

    # Example 2: Unbalanced
    root2 = list_to_tree([1, 2, None, 3, None])
    print(is_balanced(root2))  # False

    # Edge cases
    print(is_balanced(None))  # True
    print(is_balanced(TreeNode(1)))  # True

    # More complex unbalanced
    root3 = list_to_tree([1, 2, 3, 4, None, None, None, 5])
    print(is_balanced(root3))  # False
