
class Node:
    def __init__(self, data = None):
        self.nextNode = None
        self.data = data

class LinkedList:

    def __init__(self):
        self.head = None

    def printElements(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.nextNode
       

    def add(self, newData): 
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        # transverses the nodes until we hit a none value (the end)
        end = self.head
        while(end.nextNode):
            end = end.nextNode
        end.nextNode = newNode



myList = LinkedList()
myList.add(5)
myList.add(7)
myList.add(24)
myList.printElements()


