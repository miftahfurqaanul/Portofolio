class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        """Adds a child node to the current node's children list."""
        self.children.append(child_node)

    def __repr__(self, level=0):
        """Helper function to display the tree structure."""
        ret = "  " * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

    def is_leaf(self):
        """Returns True if the node is a leaf (has no children)."""
        return len(self.children) == 0

# Example Usage:
if __name__ == "__main__":
    # Creating the root node with value 90
    root = TreeNode(90)

    # Adding parent nodes with values 80 and 70 to the root
    parent1 = TreeNode(80)
    parent2 = TreeNode(70)
    root.add_child(parent1)
    root.add_child(parent2)

    # Adding child nodes to Parent 1
    child1_1 = TreeNode(60)
    child1_2 = TreeNode(50)
    parent1.add_child(child1_1)
    parent1.add_child(child1_2)

    # Adding child nodes to Parent 2
    child2_1 = TreeNode(40)
    child2_2 = TreeNode(30)
    parent2.add_child(child2_1)
    parent2.add_child(child2_2)

    # Adding leaf nodes to children
    leaf1 = TreeNode(20)
    leaf2 = TreeNode(10)
    child1_1.add_child(leaf1)
    child1_2.add_child(leaf2)

    # Display the tree structure
    print(root)

    # Checking if a node is a leaf
    # print(f"Is '{leaf1.value}' a leaf? {leaf1.is_leaf()}")
    # print(f"Is '{parent1.value}' a leaf? {parent1.is_leaf()}")
