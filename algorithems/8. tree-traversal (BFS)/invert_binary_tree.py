'''
invert_binary_tree.py
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


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    """
    Inverts a binary tree by swapping left and right children 
    for every node.
    """
    # Base case: empty tree or leaf node
    if not root:
        return None

    # Swap the children
    root.left, root.right = root.right, root.left

    # Recursively invert both subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root


def print_tree_values(root):
    """Print all values in one line with comma separator"""
    if not root:
        return

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(str(node.val))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    print(", ".join(result))


if __name__ == "__main__":
    # Example 1
    temps1 = [1, 2, 3, 4, 5, 6, 7]
    root1 = list_to_tree(temps1)
    inverted1 = invert_tree(root1)
    print_tree_values(inverted1)

    # Example 2
    temps2 = [26, 16, 5, 0, 79, 31, 9]
    root2 = list_to_tree(temps2)
    inverted2 = invert_tree(root2)
    print_tree_values(inverted2)
