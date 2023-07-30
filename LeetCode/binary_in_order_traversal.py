# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.left = left 
        self.right = right

# Input: head = [1,1,2]
# Output: [1,2]
class Solution:
    def inorderTraversal(self, root: Node) -> list[int]:
        # Recursive Approach
        stack = [root]
        while len(stack) > 0:
            cur = stack.pop()
            if cur.left != None:
                print(f"Searching left node, value: {cur.left.val}")
                stack.append(cur) # still need to explore right side
                stack.append(cur.left) # search the left node
                cur = cur.left  # New current is the left one
                print(', '.join(str(obj.val) for obj in stack))
            else: # search right
                cur = stack.pop()
                print(f"Current searching node:{cur.val}")

                

        




# A simple tree taken from https://en.wikipedia.org/wiki/Tree_traversal
nodeA = Node('A')
nodeC = Node('C')
nodeE = Node('E')
nodeH = Node('H')
nodeD = Node('D', left=nodeC, right=nodeE)
nodeI = Node('I', left=nodeH)
nodeB = Node('B', left=nodeA, right=nodeD)
nodeG = Node('G', right=nodeI)
nodeF = Node('F', left=nodeB, right=nodeG)


sol = Solution()
sol.inorderTraversal(nodeF)