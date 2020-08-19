#BINARY SEARCH TREE
from collections import deque
class TreeNode():
    def __init__(self,data):
        self.data  = data
        self.left  = None
        self.right = None
    def __str__(self):
        ans=""
        # if self.left:
        #     ans+="l {} ".format(self.left.data)
        ans+="{} ".format(self.data)
        # if self.right:
        #     ans+="r {}".format(self.right)
        return ans
class Tree():                               #Binary Search Tree
    io = ""
    def __init__(self):
        self.root = None
    def __str__(self):
            self.structure(self.root)
            return self.io
    def add(self,data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self.root = insertNode(self.root,TreeNode(data))
    def structure(self,node):
        if not node:
            self.io+=""
            return
        if node.left:
            self.structure(node.left)
        self.io+="{} ".format(node.data)
        if node.right:
            self.structure(node.right)
    def remove(self,data):
        if not self.root:
            return None
        else:
            self.root = deleteNode(self.root,data)
def insertNode(root,node):
    if not root:
        root = node
    else:
        if root.data<node.data:
            root.right = insertNode(root.right,node)
        else:
            root.left = insertNode(root.left,node)
    return root
def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print("{} ".format(root.data),end="")
    inOrder(root.right)
def preOrder(root):
    if not root:
        return
    print("{} ".format(root.data),end="")
    preOrder(root.left)
    preOrder(root.right)
def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print("{} ".format(root.data),end="")
def minRight(root):
    current = root
    while current.left:
        current = current.left
    return current
def deleteNode(root,data):
    if data<root.data:
        root.left = deleteNode(root.left,data)
    elif data>root.data:
        root.right = deleteNode(root.right,data)
    else:
        if not root.left:
            tmp = root.right
            root = None
            return tmp
        elif not root.right:
            tmp = root.left
            root= None
            return tmp
        else:
            tmp  = minRight(root.right)
            root.data = tmp.data
            root.right = deleteNode(root.right,tmp.data)
    return root
def levelOrder(root):
    x = root
    q = deque()
    q.append(x)
    q.append(0)
    while q:
        while q and q[0]!=0:
            y = q.popleft()
            print("{} ".format(y.data),end="")
            if y.left:
                q.append(y.left)
            if y.right:
                q.append(y.right)
            if q[0]==0:
                q.append(0)
        if q[0]==0:
            q.popleft()
def height(root):
    if not root:
        return 0
    else:
        return max(height(root.left),height(root.right))+1
def size(root):
    if not root:
        return 0
    else:
        return size(root.left)+size(root.right)+1
t1 = Tree()
t1.add(0)
t1.add(5)
t1.add(-1)
t1.add(4)
t1.add(6)
t1.add(4.5)
t1.add(1)
t1.add(2)
t1.add(9)
t1.add(8)
# preOrder(t1.root)
# print("")
t1.remove(2)
# preOrder(t1.root)
# print("")
t1.add(-3)
t1.add(0.5)
t1.add(-4)
t1.remove(-3)
# preOrder(t1.root)
# print("")
t1.add(4.2)
t1.remove(4)
# preOrder(t1.root)
# print("")
print(height(t1.root))
print("size:{} ".format(size(t1.root)))
preOrder(t1.root)
print("")
levelOrder(t1.root)