
# implementation of digraph
class digraph:
    def __init__(self, v):
        self.V = v
        self.arr = [None] * v

    def __str__(self):
        s = ""
        for i in range(self.V):
            if not self.arr[i]:
                s += "\n" + "None"
            else:
                s += "\n" + str(i) + "-->" + str(self.arr[i])
        return s
    def __repr__(self):
        return str(self)

    def addEdge(self, v, w):
        if not self.arr[v]:
            self.arr[v] = Linked_List()
        if not self.arr[w]:
            self.arr[w] = Linked_List()
        self.arr[v].add(w)

    def adj(self, v):
        return self.arr[v]



class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        s = ""
        walk = self.head
        while walk:
            s += " " + str(walk.value)
            walk = walk.next
        return s


    def add(self, val):
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
