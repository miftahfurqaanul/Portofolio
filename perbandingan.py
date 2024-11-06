import random
import time

def create_array(n):
    return [random.randint(1, 1000) for _ in range(n)]

def create_bst(data):
    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data

    def insert(node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = insert(node.left, data)
        else:
            node.right = insert(node.right, data)
        return node

    root = None
    for i in data:
        root = insert(root, i)
    return root

def search_array(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return True
    return False

def search_bst(root, x):
    if root is None:
        return False
    if root.data == x:
        return True
    elif x < root.data:
        return search_bst(root.left, x)
    else:
        return search_bst(root.right, x)

# Generate random data
n = 10000
data = create_array(n)

# Create array and BST
arr = data.copy()
bst = create_bst(data)

# Search for random elements
for _ in range(1000):
    x = random.randint(1, 1000)

    # Measure time for array search
    start_time = time.time()
    result = search_array(arr, x)
    end_time = time.time()
    array_time = end_time - start_time

    # Measure time for BST search
    start_time = time.time()
    result = search_bst(bst, x)
    end_time = time.time()
    bst_time = end_time - start_time

    print(f"Array time: {array_time:.6f} seconds")
    print(f"BST time: {bst_time:.6f} seconds")