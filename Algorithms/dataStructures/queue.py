class Node:
    def __init__(self, data = None):
        self.next = None
        self.data = data

class Queue:

    def __init__(self):
        self.first = None
        self.last = None

    def printElements(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def enqueue(self, newData): 
        if (self.first == None):
            self.last = newData
            self.first = self.last
        else:
            self.last.next = newData
            self.last = self.last.next

    def dequeue(self):
        if (self.first != None):
            temp = self.first.data
            self.first = self.first.next
            return temp
        return None




queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
print(queue.dequeue())


