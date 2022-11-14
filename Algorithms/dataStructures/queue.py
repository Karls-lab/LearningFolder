# Queue Class Using a Node Class
# FIFO data strucutre
# Implemented in Python by Karl

class Node:
    def __init__(self, data = None):
        self.next = None
        self.data = data

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def printElements(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def enqueue(self, newData):
        newNode = Node(newData)
        if (self.head == None):
            self.tail = newNode
            self.head = self.tail
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

    def dequeue(self):
        if (self.head != None):
            temp = self.head.data
            self.head = self.head.next
            return temp
        return None




queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.dequeue()
queue.dequeue()
#print(queue.dequeue())
queue.printElements()


