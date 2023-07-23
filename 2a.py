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
root = Node("Faza")
root.left = Node("Yoga" )
root.right = Node("Ardana")
# root.left.left = Node("Septin")
# root.left.right = Node("David")
# root.right.left = Node("Eva")
# root.right.right = Node("Frank")

print("Preorder traversal:")
preorder_traversal(root)
print("\n")

print("Inorder traversal:")
inorder_traversal(root)
print("\n")

print("Postorder traversal:")
postorder_traversal(root)
print("\n")
