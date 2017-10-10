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
        bst._insert(root, data)

    def _insert(root, data)
        if root is None:
            return node(data)
        else:
            if data < root.data:
                root.left = bst._insert(root.left, data)
            else:
                root.right = bst._insert(root.right, data)

        return root

    def erase(self, data):
        pass

    def search(self, data):
        pass

    def part(self, data):
        pass

    def bfs(self):
        pass

    def inoderR(self):
        bst._inorder(self.root)

    def _inorder(root):
        if root:
            bst._inorder(self.left)
            print(root.data, end=' ')
            bst._inorder(self.right)

    def preorderR(self):
        pass

    def postorderR(self):
        pass

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
        t.insertI(i)

    t.printSideway()
