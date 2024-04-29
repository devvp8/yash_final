class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_diameter_and_height(root):
    """
    Finds the diameter and height of a binary search tree.

    Args:
        root (Node): The root node of the binary search tree.

    Returns:
        tuple: A tuple containing the diameter and height of the binary search tree.
    """

    # Base case: If the tree is empty, the diameter and height are both 0.
    if root is None:
        return 0, 0

    # Recursively find the diameter and height of the left and right subtrees.
    left_diameter, left_height = find_diameter_and_height(root.left)
    right_diameter, right_height = find_diameter_and_height(root.right)

    # The diameter of the tree is the maximum of the following three values:
    # 1. The diameter of the left subtree
    # 2. The diameter of the right subtree
    # 3. The height of the left subtree + the height of the right subtree + 1
    diameter = max(left_diameter, right_diameter, left_height + right_height + 1)

    # The height of the tree is the maximum of the following two values:
    # 1. The height of the left subtree
    # 2. The height of the right subtree
    height = max(left_height, right_height) + 1

    # Return the diameter and height of the tree.
    return diameter, height


# Test the find_diameter_and_height function.
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

diameter, height = find_diameter_and_height(root)
print("Diameter:", diameter)
print("Height:", height)