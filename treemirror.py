from queue import Queue
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def levelOrderTraversal(root):
    if not root:
        return
    q = []
    #Insert at front is done because, list.pop pops from the end
    q.insert(0, root)
    while len(q) > 0:
        e = q.pop()
        print(e.data, end = " ")
        if e.left:
            q.insert(0, e.left)
        if e.right:
            q.insert(0, e.right)
    print(end="\n")

def treeMirror(root):
    if root:
        temp1 = treeMirror(root.left)
        temp2 = treeMirror(root.right)
        root.left, root.right = temp2, temp1

    return root

def test1():
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)


    levelOrderTraversal(root)
    root = treeMirror(root)
    levelOrderTraversal(root)

def test2():
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    levelOrderTraversal(root)
    root = treeMirror(root)
    levelOrderTraversal(root)

test1()
test2()