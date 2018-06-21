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
    PrintBoundaryLeftUtil(t.left, True)
    PrintBoundaryRightUtil(t.right, True)
    print()

def PrintBoundaryLeftUtil(l,isPrint):
    if l is None:
        return

    if isPrint or (l.left is None and l.right is None):
        print(l.val, end=" ")
    if l.left:
        PrintBoundaryLeftUtil(l.left, True)
        PrintBoundaryLeftUtil(l.right, False)
    elif l.right:
        PrintBoundaryLeftUtil(l.right, True)

def PrintBoundaryRightUtil(r, isPrint):
    if r is None:
        return

    if r.right:
        PrintBoundaryRightUtil(r.left, False)
        PrintBoundaryRightUtil(r.right, True)
    elif r.left:
        PrintBoundaryRightUtil(r.left, True)
    if isPrint or (r.left is None and r.right is None):
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
