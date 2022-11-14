class Node:
    def __init__(self, data = None):
        self.next = None
        self.data = data

class Stack:

    def __init__(self):
        self.top = None

    def printElements(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def peek(self):
        return self.top.data

    def push(self, newData): 
        newNode = Node(newData)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if (self.top != None):
            temp = self.top.data
            self.top = self.top.next
            return temp
        return None




stack = Stack()
stack.push(5)
stack.push(4)
print(stack.peek())
stack.pop()
print(stack.peek())


