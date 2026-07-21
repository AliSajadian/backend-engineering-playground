'''
diameter_of_binary_tree.py
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


class TreeDiameter:
    '''
    Calculate Tree Diameter
    '''
    def __init__(self):
        self.diameter = 0 # Global variable (or use nonlocal in nested function)

    def diameter_of_binary_tree(self, root: TreeNode | None) -> int:
        """
        Returns the diameter (longest path in edges) of a binary tree.
        """
        self.diameter = 0

        def depth(node: TreeNode | None) -> int:
            '''
            Calculate tree node longest diameter
            '''
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.diameter


if __name__ == "__main__":
# Example: [3,9,20,None,None,15,7]
    sample_root = list_to_tree([3, 9, 20, None, None, 15, 7])
    print(TreeDiameter().diameter_of_binary_tree(sample_root))  # Output: 3

    # Edge cases
    print(TreeDiameter().diameter_of_binary_tree(None))  # Output: 0
    print(TreeDiameter().diameter_of_binary_tree(TreeNode(1)))  # Output: 1
    print(TreeDiameter().diameter_of_binary_tree(list_to_tree([1, 2, 3, 4])))  # Output: 3
