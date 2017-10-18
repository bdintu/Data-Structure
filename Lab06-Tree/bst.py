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

    def _insert(cur, data):
        if cur is None:
            return node(data)
        else:
            if data < cur.data:
                cur.left = bst._insert(cur.left, data)
            else:
                cur.right = bst._insert(cur.right, data)

        return cur

    def count(self, parent):
        i = 0
        if parent:
            if parent.left:
                i += 1
            if parent.right:
                i += 1
        return i

    def eraseR(self, data):
        parent = self.searchParentI(data)
        child = self.searchI(data)
        if self.count(child):
            if parent.left and parent.left.data == data:
                parent.left = None
            elif parent.right and parent.right.data == data:
                parent.right = None

        elif self.count(child) == 1:
            if chile.left:
                parent
                

    def searchI(self, data):
        cur = self.root
        while cur:
            if data < cur.data:
                cur = cur.left
            elif data > cur.data:
                cur = cur.right
            else:
                return cur
        
        return None

    def searchR(self, data)
        return bst._search(self.root, data)

    def _search(cur, data)
        if cur == None:
            return None
        elif data < cur.data:
            return bst._search(cur.left, data)
        elif data > cur.data:
            return bst._search(cur.right, data)
        else:
            return cur

    def searchParentI(self, data):
        cup = None
        cur = self.root
        while cur:
            if data < cur.data:
                cur = cur.left
            elif data > cur.data:
                cur = cur.right
            else:
                return cup

            cup = cur
        
        return None

    def searchParentR(self, data)
        return bst._search(self.root, data)

    def _searchParent(cur, data)
        if cur == None:
            return None
        elif data < cur.data:
            return bst._search(cur.left, data)
        elif data > cur.data:
            return bst._search(cur.right, data)
        else:
            return cur

    def pathI(self, data):
        cur = self.root
        while cur:
            print(cur.data, end=' ')
            if data < cur.data:
                cur = cur.left
            elif data > cur.data:
                cur = cur.right

    def pathR(self, data):
        bst._path(self.root, data)

    def _path(cur, data):
        print(cur.data, end=' ')
        if cur == None:
            return
        elif data < cur.data:
            bsr._path(cur.left, data)
        elif data > cur.data:
            bst._path(cur.right, data)

    def bfs(self):
        stack = [self.root]

    def inorderR(self):
        bst._inorder(self.root)

    def _inorder(cur):
        if cur:
            bst._inorder(cur.left)
            print(cur.data, end=' ')
            bst._inorder(cur.right)

    def preorderR(self):
        bst._preorder(self.root)

    def _preorder(cur):
        if cur:
            print(cur.data, end=' ')
            bst._preorder(cur.left)
            bst._preorder(cur.right)

    def postorderR(self):
        bst._postorder(self.root)

    def _postorder(cur):
        if cur:
            bst._postorder(cur.left)
            bst._postorder(cur.right)
            print(cur.data, end=' ')

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
    
    print("inOrder Iter : ")
    t.inorderR()
    print("inOrder Rec  : ")
    tR.inorderR()

    print("\npath %s: "%l[5], end='')
    t.path(l[5])
