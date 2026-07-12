'''
maximum_depth_of_binary_tree.py
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


def max_depth(root: TreeNode | None) -> int:
    '''
    Retrieve the length of the longest root-to-leaf path.
    '''
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
# Example: [3,9,20,None,None,15,7]
    sample_root = list_to_tree([3, 9, 20, None, None, 15, 7])
    print(max_depth(sample_root))  # Output: 3

    # Edge cases
    print(max_depth(None))  # Output: 0
    print(max_depth(TreeNode(1)))  # Output: 1
    print(max_depth(list_to_tree([1, 2, 3, 4])))  # Output: 3
