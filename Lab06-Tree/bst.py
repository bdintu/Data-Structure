from node import node

class bst:
    def __init__(self, root=None):
        self.root = root

    def insertI(self, data):
        n = node(data)

        if self.root is None:
            self.root = n

        else:
            parent = None
            child = self.root

            while child:
                parent = child
                if data < child.data:
                    child = child.left
                else:
                    child = child.right

            if data < parent.data:
                parent.left = n
            else:
                parent.right = n

    def insertR(self, data):
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

    def count(self, parent):
        i = 0
        if parent:
            if parent.left:
                i += 1
            if parent.right:
                i += 1
        return i

    def eraseR(self, data):
        bst._erase(self.root, data)

    def _erase(root, data):
        if not root:
            return None

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

    def searchI(self, data):
        root = self.root
        while root:
            if data < root.data:
                root = root.left
            elif data > root.data:
                root = root.right
            else:
                return root
        
        return None

    def searchR(self, data):
        return bst._search(self.root, data)

    def _search(root, data):
        if root is None:
            return None
        elif data < root.data:
            return bst._search(root.left, data)
        elif data > root.data:
            return bst._search(root.right, data)
        else:
            return root

    def pathI(self, data):
        root = self.root
        while root:
            print(root.data, end=' ')
            if data < root.data:
                root = root.left
            elif data > root.data:
                root = root.right

    def pathR(self, data):
        bst._path(self.root, data)

    def _path(root, data):
        print(root.data, end=' ')
        if root is None:
            return
        elif data < root.data:
            bst._path(root.left, data)
        elif data > root.data:
            bst._path(root.right, data)

    def bfs(self):
        stack = [self.root]

    def inorderR(self):
        bst._inorder(self.root)

    def _inorder(root):
        if root:
            bst._inorder(root.left)
            print(root.data, end=' ')
            bst._inorder(root.right)

    def preorderR(self):
        bst._preorder(self.root)

    def _preorder(root):
        if root:
            print(root.data, end=' ')
            bst._preorder(root.left)
            bst._preorder(root.right)

    def postorderR(self):
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
    tR = bst()

    l = [14,4,9,7,15,3,18,16,20,5,16]
    for i in l:
        t.insertI(i)
        tR.insertR(i)
    
    print("\ninOrder Iter : ")
    t.inorderR()
    print("\ninOrder Rec  : ")
    tR.inorderR()

    print("print sideway")
    tR.printSideway();

    print("\npath %s: "%l[5], end='')
    t.pathR(l[5])

    tR.eraseR(9)

    print("print sideway")
    tR.printSideway();
