class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def isLeaf(self):
        if self.left == None and self.right == None:
            return True
        return False

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def hasBothChildren(self):
        return self.left and self.right

    def findSuccessor(self):
        # find min of right subtree
            succ = None
            if self.hasRightChild():
                succ = self.right.findMin()
                return succ
            else:
                if self.parent:
                    if self.isLeftChild():
                        succ = self.parent
                    else:
                        self.parent.right = None
                        succ = self.parent.findSuccessor()
                        self.parent.right = self

            return succ

    def hasLeftChild(self):
        return True if self.left else False

    def hasRightChild(self):
        return True if self.right else False

    def hasAnyChildren(self):
        return True if self.right or self.left else False

    def findMin(self):
        curr = self
        while curr.hasLeftChild():
            curr = curr.left
        return curr

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None

        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.left
                else:
                    self.parent.rightChild = self.left
                self.left.parent = self.parent
        else:
            if self.isLeftChild():
                self.parent.leftChild = self.right
            else:
                self.parent.rightChild = self.right
            self.right.parent = self.parent


class bst():

    def __init__(self):
        self.root = Node(None)

    def insert(self, data):
        if self.root.val is None:
            self.root = Node(data)

        else:
            self.insertNode(self.root, data)

    def insertNode(self, node, data):
        if data <= node.val:
            if node.left:
                self.insertNode(node.left, data)
            else:
                newNode = Node(data)
                node.left = newNode
                newNode.parent = node

        else:
            if node.right:
                self.insertNode(node.right, data)
            else:
                newNode = Node(data)
                node.right = newNode
                newNode.parent = node

    def get(self, data):
        node = self.root
        while node:
            if node.val < data:
                node = node.right
            elif node.val > data:
                node = node.left
            else:
                return node
        return None


    def min(self):
        node = self.root
        while node:
            node = node.left
        return node.val

    # floor: largest val <= given val
    # def floor(self, val):
    #     if self.root is None:
    #         return None
    #     if self.root.val == val:
    #         return self.root
    #
    #     elif self.root.val > val:
    #         return self.floor(self.root.left, val)
    #
    #     t = self.floor(self.root.right, val)
    #     if t is not None: return t
    #     else: return self.root


    def delete(self, data):
        nodeToDelete = self.get(data)
        self.remove(nodeToDelete)

    def remove(self, currentNode):
    # delete with no children
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None

    # delete with two children
        elif currentNode.hasBothChildren():
            # find successor
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.val = succ.val

    # delete with one child
        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                elif currentNode.isRightChild():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.right = currentNode.left
                else:
                    currentNode.replaceData(currentNode.left.val, currentNode.left.left, currentNode.left.right)
            else:
                if currentNode.isLeftChild():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.left = currentNode.right
                elif currentNode.isRightChild():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.right = currentNode.right
                else:
                    currentNode.replaceData(currentNode.right.val, currentNode.right.left, currentNode.right.right)





    def inorder(self):
        if self.root:
            self.inorder(self.root.left)
            print(self.root.val)
            self.inorder(self.root.right)