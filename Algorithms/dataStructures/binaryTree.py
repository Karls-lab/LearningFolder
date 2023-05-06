class Node:
    def __init__(self, key = None):
        self.right = None
        self.left = None
        self.key = key



def insert(node, root):
    if root is None:
        print("node inserting is " + str(node.key))
        return node
    
    else:
        print("here")
        if node.key < root.key:
            print("root left = " + str(root.left))
            root.left = insert(node, root.left)
            print("root left now equals = " + str(root.left))
        if node.key > root.key:
            root.right = insert(node, root.right)
            
    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)


root = Node(3)
insert(Node(2), root)
insert(Node(1), root)
insert(Node(4), root)

inorder(root)


        
