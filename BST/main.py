from BST.bst import *

b = bst()
b.insert(3)
b.insert(1)
b.insert(5)
print(b.get(5))
print(b.root.val)
print(b.root.left.val)
print(b.root.right.val)
b.insert(4)
b.insert(6)
b.delete(5)
print(b.root.val)
print(b.root.left.val)
print(b.root.right.val)
print(b.root.right.left.val)