from collections import deque
from node import node

class bst:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        self.root = bst._insert(self.root, data)

    def _insert(root, data):
        if not root:
            return node(data)
        else:
            if data < root.data:
                root.left = bst._insert(root.left, data)
            else:
                root.right = bst._insert(root.right, data)

        return root

    def erase(self, data):
        bst._erase(self.root, data)

    def _erase(root, data):
        if not root:
            return

        if root.data > data:
            root.left = bst._erase(root.left, data)
        elif root.data < data:
            root.right = bst._erase(root.right, data)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                successor = root.right
                while successor.left:
                    successor = successor.left

                root.data = successor.data
                root.right = bst._erase(root.right, successor.data)

        return root

    def search(self, data):
        return bst._search(self.root, data)

    def _search(root, data):
        if not root:
            return
        elif data < root.data:
            return bst._search(root.left, data)
        elif data > root.data:
            return bst._search(root.right, data)
        else:
            return root

    def path(self, data):
        bst._path(self.root, data)

    def _path(root, data):
        if not root:
            return
        
        print(root, end=' ')
        
        if data < root.data:
            bst._path(root.left, data)
        elif data > root.data:
            bst._path(root.right, data)

    def depth(self, data):
        return bst._depth(self.root, data)

    def _depth(root, data):
        if not root:
            return
        elif data < root.data:
            return bst._depth(root.left, data) + 1
        elif data > root.data:
            return bst._depth(root.right, data) + 1
        else:
            return 0

    def maxDepth(self):
        return bst._maxdepth(self.root)

    def high(self, root): 
        return bst._maxdepth(root)

    def _maxdepth(root):
        if root:
            return max(bst._maxdepth(root.left)+1, bst._maxdepth(root.right)+1)
        else:
            return -1

    def bfs(self):
        stack = deque()
        stack.append(self.root)
        
        while(stack):
            root = stack.popleft()
            print(root, end=' ')
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)            

    def inorder(self):
        bst._inorder(self.root)

    def _inorder(root):
        if root:
            bst._inorder(root.left)
            print(root.data, end=' ')
            bst._inorder(root.right)

    def preorder(self):
        bst._preorder(self.root)

    def _preorder(root):
        if root:
            print(root.data, end=' ')
            bst._preorder(root.left)
            bst._preorder(root.right)

    def postorder(self):
        bst._postorder(self.root)

    def _postorder(root):
        if root:
            bst._postorder(root.left)
            bst._postorder(root.right)
            print(root.data, end=' ')

    def printSideway(self):
        bst._siderway(self.root, 0)

    def _siderway(root, level):
        if root:
            bst._siderway(root.right, level+1)
            print(' '*3*level, root.data)
            bst._siderway(root.left, level+1)

if __name__ == "__main__":
    t = bst()

    l = [14,4,9,7,15,3,18,16,20,5,16]
    for i in l:
        t.insert(i)

    print("print sideway  : ")
    t.printSideway();
   
    print("\ninOrder  : ", end=' ')
    t.inorder()
    print("\npreOrder : ", end=' ')
    t.preorder()
    print("\npostOrder: ", end=' ')
    t.postorder()
    print("\nbfs      : ", end=' ')
    t.bfs()    

    print("\nmaxDepth : ", t.maxDepth())

    n = l[5]
    nod = t.search(n)
    if nod:
        print("search %d : "%n, nod.data)
        print("high %d   : "%n, t.high(nod))
    print("depth %d  : "%n, t.depth(n))
    print("path %d   : "%n, end='')
    t.path(n)

    print("\nerase %d  : "%n)
    t.erase(n)
    t.printSideway()
