"""
Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root.

https://www.dropbox.com/s/8zf85nhbzpox2nh/BoundryTraversal.gif?dl=0

20 8 4 10 14 25 22
1. Print all left nodes

2. If left=null,
   print right and its left tree
   if not left, print right
3. Print All right nodes
   if right = null, print rightmost of right tree
4. Print all leaf nodes

printBoundary(Tree):
1. If (null) return
   printBoundaryUtil(node.left, 'l')
   printBoundaryUtil(node.right, 'r')

printBounddaryUtil(Tree, side = 'l' or 'r'):
    // If leaf node
    if node.left == none and node.right == none:
     print node.value
     return

1. if side = 'l' and node.left != none

    printBoundary(node.left, 'l')
   else
    printBoundary(node.right,'l')
2. if side = 'r' and node.right ! = none
    printBoundary(node.right, 'r')
   else
    printBoundary(node.left, 'r')
"""
class Tree:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def PrintBoundary(t):
    if t is None:
        return

    print(t.val, end=" ")
    PrintBoundaryLeftUtil(t.left)
    PrintLeafUtil(t.left)
    PrintLeafUtil(t.right)
    PrintBoundaryRightUtil(t.right)
    print()

def PrintBoundaryLeftUtil(l):
    if l is None:
        return

    if l.left:
        print(l.val, end=" ")
        PrintBoundaryLeftUtil(l.left)
    elif l.right:
        print(l.val, end=" ")
        PrintBoundaryLeftUtil(l.right)

def PrintLeafUtil(t):
   if t:
       if t.left is None and t.right is None:
           print (t.val, end=" ")
           return

       if(t.left):
            PrintLeafUtil(t.left)
       if (t.right):
            PrintLeafUtil(t.right)


def PrintBoundaryRightUtil(r):
    if r is None:
        return

    if r.right:
        PrintBoundaryRightUtil(r.right)
        print(r.val, end = " ")
    elif r.left:
        PrintBoundaryRightUtil(r.left)
        print(r.val, end = " ")


def TestCase1():
    root = Tree(20)
    root.left = Tree(8)
    root.left.left = Tree(4)
    root.left.right = Tree(12)
    root.left.right.left =  Tree(10)
    root.left.right.right = Tree(14)
    root.right = Tree(22)
    root.right.right = Tree(25)

    PrintBoundary(root)


def TestCase2():
    root = Tree(20)
    root.left = Tree(8)
    root.left.left = Tree(4)
    root.left.right = Tree(12)
    root.left.right.left =  Tree(10)
    root.left.right.right = Tree(14)
    root.right = Tree(22)
    root.right.left = Tree(28)
    root.right.right = Tree(25)

    PrintBoundary(root)

def TestCase3():
    root = Tree(20)
    root.left = Tree(8)
    #root.left.left = Tree(4)
    root.left.right = Tree(12)
    root.left.right.left =  Tree(10)
    root.left.right.right = Tree(14)
    root.right = Tree(22)
    root.right.left = Tree(28)
    root.right.right = Tree(25)

    PrintBoundary(root)

TestCase1()
TestCase2()
TestCase3()
