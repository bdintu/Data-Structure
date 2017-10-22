from node import node

class bst:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        self.root = bst._insert(self.root, data)

    def _insert(root, data):
        if root is None:
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
        if root is None:
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
        print(root.data, end=' ')
        if root is None:
            return
        elif data < root.data:
            bst._path(root.left, data)
        elif data > root.data:
            bst._path(root.right, data)

    def depth(self, data):
        return bst._depth(self.root, data)

    def _depth(root, data, depth=0):
        if root is None:
            return
        elif data < root.data:
            return bst._depth(root.left, data, depth+1)
        elif data > root.data:
            return bst._depth(root.right, data, depth+1)
        else:
            return depth

    def maxDepth(self):
        return bst._maxdepth(self.root)

    def high(self, root): 
        return bst._maxdepth(root)

    def _maxdepth(root, depth=-1):
        if root:
            return max(bst._maxdepth(root.left, depth+1), bst._maxdepth(root.right, depth+1))
        else:
            return depth

    def bfs(self):
        stack = [self.root]

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
   
    print("\ninOrder Iter   : ", end=' ')
    t.inorder()
    print("\npreOrder Iter  : ", end=' ')
    t.preorder()
    print("\npostOrder Iter : ", end=' ')
    t.postorder()

    print("\nmaxDepth : ", t.maxDepth())

    n = l[5]
    nod = t.search(n)
    print("search %d : "%n, nod)
    print("high %d   : "%n, t.high(nod))
    print("depth %d  : "%n, t.depth(n))
    print("path %d   : "%n, end='')
    t.path(n)

    print("\nerase %d  : "%n)
    t.erase(n)
    t.printSideway()
