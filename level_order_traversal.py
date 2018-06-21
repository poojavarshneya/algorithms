from collections import defaultdict
from queue import Queue

class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def insertNode(self, val):
        node = LinkedNode(val)
        if self.root is None:
            self.root = node
            return

        root = self.root
        while root.next:
            root = root.next
        root.next = node

    def print(self):
        root = self.root
        while (root):
            print(root.data, end = " ")
            root = root.next
        print(end = "\n")

class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None

def levelOrderTraversalWithLists(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    #result = defaultdict(list)
    result = []
    if not root:
        return result
    nodes = [root]
    while nodes:
        vals, nodes_next = [],[]
        for node in nodes:
            vals.append(node.val)
            if (node.left):
                nodes_next.append(node.left)
            if (node.right):
                nodes_next.append(node.right)
        nodes = nodes_next
        result.append(vals)
    return result

def levelOrderTraversalWithLinkedLists(root):
    result = []
    if root is None:
        return result

    nodes = [root]
    while nodes:
        ll_result = LinkedList()
        node_next = []
        for node in nodes:
            ll_result.insertNode(node.val)
            if node.left:
                node_next.append(node.left)
            if node.right:
                node_next.append(node.right)
        nodes = node_next
        result.append(ll_result)
    return result

def test1():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)


    result = levelOrderTraversalWithLists(root)
    print(result)
    result = levelOrderTraversalWithLinkedLists(root)
    for ll in result:
        ll.print()

test1()
