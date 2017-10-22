from node import node

class bsti:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
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

    def search(self, data):
        root = self.root

        while root:
            if data < root.data:
                root = root.left
            elif data > root.data:
                root = root.right
            else:
                return root
        
        return None

    def path(self, data):
        root = self.root

        while root:
            print(root.data, end=' ')
            if data < root.data:
                root = root.left
            elif data > root.data:
                root = root.right
