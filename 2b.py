class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node is not None:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=" ")

# Membangun pohon biner
root = Node("2023123456")
root.left = Node("2023123455")
root.right = Node("2023123457")
root.left.left = Node("2023123454")
root.left.right = Node("2023123453")
root.right.left = Node("2023123458")
root.right.right = Node("2023123459")

print("Preorder traversal:")
preorder_traversal(root)
print("\n")

print("Inorder traversal:")
inorder_traversal(root)
print("\n")

print("Postorder traversal:")
postorder_traversal(root)
print("\n")
