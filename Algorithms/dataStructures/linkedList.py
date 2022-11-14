class Node:
    def __init__(self, data = None):
        self.next = None
        self.data = data

class LinkedList:

    def __init__(self):
        self.head = None

    def printElements(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
       

    def add(self, newData): 
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        # transverses the nodes until we hit a none value (the end)
        end = self.head
        while(end.next):
            end = end.next
        end.next = newNode

    def delete(self, data):
        temp = self.head
        if(temp.data == data):
            print("data is head")
        while(temp != None):
            prev = temp
            temp = temp.next
            if(temp.data == data):
                prev.next = temp.next
                return self.head
        return self.head



myList = LinkedList()
myList.add(5)
myList.add(7)
myList.add(24)
myList.add(60)
myList.add(42)
myList.delete(24)
myList.printElements()


