# Romain Tranchant
# CIS 103 Fundamentals of Programming
# Instructor: MD Ali
# Christmas Tree



# Import the random module for random decoration selection
import random

# Define a Node class for the binary tree structure
class Node:
    def __init__(self, value):
        self.left = None  # Initialize the left child as None
        self.right = None  # Initialize the right child as None
        self.value = value  # Set self.value to the parameter value

# Define a function to build the Christmas tree with the specified number of levels
def build_christmas_tree(levels):
# Create the root node with the top decoration
    root = Node("*")
# Initialize the current level with the root node
    current_level = [root]

# Loop through the levels to build the tree
    for _ in range(1, levels):
# Initialize the next level as an empty list
        next_level = []
# Loop through the nodes in the current level
        for node in current_level:
# Randomly select decorations for the left and right children
            node.left = Node(random.choice(["@", "$", "*", "+"]))
            node.right = Node(random.choice(["@", "$", "*", "+"]))
# Add the children to the next level
            next_level.extend([node.left, node.right])
# Move to the next level
        current_level = next_level
# Return the root of the tree
    return root

# Define a function to visualize the tree structure
def visualize_tree(root, levels):
    if not root:
        return

# Initialize a queue with the root node
    queue = [root]
# Loop through each level to print the tree
    for level in range(levels):
# Calculate the number of nodes at the current level
        level_node = 2 ** level
# Calculate the padding for the current level
        padding = " " * (levels - level - 1)
# Initialize the line with padding
        line = padding

# Loop through the nodes at the current level
        for _ in range(level_node):
            if queue:
# Dequeue the first node
                current = queue.pop(0)
# Append the current node's value
                line += current.value + " "
# Enqueue the left and right children if they exist
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            else:
                line += " "
# Print the current level line
        print(line)

# Define the number of levels for the Christmas tree
levels = 5

# Build the Christmas tree with the specified levels
tree_root = build_christmas_tree(levels)

# Visualize the constructed Christmas tree
visualize_tree(tree_root, levels)
