# Romain Tranchant
# CIS 103 Fundamentals of Programming
# Instructor: MD Ali
# Binary Tree Operations

# Root is the top element
# Left node and right node
# Sorted, kinda like the binary search algorithm
# Each node has at most 2 children
# Hierarchical data

# Define a Node class for the binary tree
class Node:
    def __init__(self, key):
        self.left = None
# Initialize left child as None
        self.right = None
# Initialize right child as None
        self.val = key
# Initialize node value

# Define inorder traversal function
def inorder_traversal(node):
    if node:  # If the node is not None
        inorder_traversal(node.left)  # Traverse the left subtree
        print(node.val, end= " ")  # Print the node value
        inorder_traversal(node.right)  # Traverse the right subtree

# Define preorder traversal function
def preorder_traversal(node):
    if node:  # If the node is not None
        print(node.val, end= " ")  # Print the node value
        preorder_traversal(node.left)  # Traverse the left subtree
        preorder_traversal(node.right)  # Traverse the right subtree

# Define postorder traversal function
def postorder_traversal(node):
    if node:  # If the node is not None
        postorder_traversal(node.left)  # Traverse the left subtree
        postorder_traversal(node.right)  # Traverse the right subtree
        print(node.val, end= " ")  # Print the node value

# Create the root of the binary tree
root = Node(5)
# Add left and right children to the root
root.left = Node(3)
root.right = Node(7)
# Add children to the left node of the root
root.left.left = Node(2)
root.left.right = Node(4)
# Add children to the right node of the root
root.right.left = Node(6)
root.right.right = Node(8)

# Perform inorder traversal and print the nodes
print("Inorder traversal:")
inorder_traversal(root)  # Output: 2 3 4 5 6 7 8

# Perform preorder traversal and print the nodes
print("\n\nPreorder Traversal:")
preorder_traversal(root)  # Output: 5 3 2 4 7 6 8

# Perform postorder traversal and print the nodes
print("\n\nPostorder Traversal:")
postorder_traversal(root)  # Output: 2 4 3 6 8 7 5

# Define a function to calculate the height of the tree
def tree_height(node):
    if node is None:  # If the node is None, the height is 0
        return 0
    # Calculate the height of the left and right subtrees and add 1
    return max(tree_height(node.left), tree_height(node.right)) + 1

# Define a function to check if the tree is a Binary Search Tree (BST)
def is_bst(node, min_value=float('-inf'), max_value=float('inf')):
    if node is None:  # If the node is None, it is a BST
        return True
    if not(min_value < node.val < max_value):  # Check the BST property
        return False
# Check recursively for left and right subtrees
    return is_bst(node.left, min_value, node.val) and is_bst(node.right, node.val, max_value)

# Define a function for level order traversal of the tree
def level_order_traversal(root):
    if root is None:  # If the root is None, return an empty list
        return []
    queue = [root]  # Initialize a queue with the root
    result = []  # Initialize an empty result list
    while queue:  # While the queue is not empty
        current = queue.pop(0)  # Dequeue the first element
        result.append(current.val)  # Add the current node's value to the result
        if current.left:  # If the left child exists, enqueue it
            queue.append(current.left)
        if current.right:  # If the right child exists, enqueue it
            queue.append(current.right)
    return result  # Return the level order traversal result

# Check if the tree is a Binary Search Tree (BST) and print the result
print("\n\nIs it a Binary Search Tree?", is_bst(root, float('-inf') , float('inf')))  # Output: True

# Perform level order traversal and print the result
print("\nLevel order Traversal:", level_order_traversal(root))  # Output: [5, 3, 7, 2, 4, 6, 8]
