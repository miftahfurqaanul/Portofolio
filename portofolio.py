## Data Structure Array
print("============  Array Search  ============")
import sys

def linear_search(array, target):
    """Performs linear search on a system array.

    Args:
        array: The system array to search.
        target: The value to search for.

    Returns:
        The index of the target value in the array, or -1 if not found.
    """

    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

def binary_search(array, target):
    """Performs binary search on a sorted system array.

    Args:
        array: The sorted system array to search.
        target: The value to search for.

    Returns:
        The index of the target value in the array, or -1 if not found.
    """

    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
system_array = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 50

# Linear search
index = linear_search(system_array, target)
if index != -1:
    print(f"{target} found at index {index} using linear search.")
else:
    print(f"{target} not found using linear search.")

# Binary search (array must be sorted)
system_array.sort()  # Ensure the array is sorted
index = binary_search(system_array, target)
if index != -1:
    print(f"{target} found at index {index} using binary search.")
else:
    print(f"{target} not found using binary search.")

print()
print("======  Contoh Array ke-1  ===========")
# Membuat array (list)
my_array = [10, 20, 30, 40]

# Mengakses elemen
print(my_array[0])  # Output: 10

# Mengubah elemen
my_array[2] = 50
print(my_array)  # Output: [10, 20, 50, 40]

# Menambahkan elemen
my_array.append(60)
print(my_array)  # Output: [10, 20, 50, 40, 60]

# Menghapus elemen
del my_array[1]
print(my_array)  # Output: [10, 50, 40, 60]
print()

##contoh 2
print("======  Contoh Array ke-2  ===========")

# Membuat array berisi nama-nama buah
print()
fruits = ["apple", "banana", "orange"]

# Menampilkan semua buah
for fruit in fruits:
    print(fruit)

# Mencari buah tertentu (misalnya, "banana")
if "banana" in fruits:
    print("Buah banana ada dalam daftar")

print()
print("=======  Data Structure non linier Trees  =========")
print()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

def  search(root, data):
    if root is None:
        return False
    if root.data == data:
        return True
    elif data < root.data:
        return search(root.left, data)
    else:
        return search(root.right, data)

# Create a sample binary search tree
root = insert(None, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

# Inorder traversal (prints the elements in sorted order)
print("Inorder Traversal:")
inorder_traversal(root)
print()

# Search for an element
x = 40
if search(root, x):
    print(f"{x} found in the tree.")
else:
    print(f"{x} not found in the tree.")


