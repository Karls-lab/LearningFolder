"""
Karl's implementation of 'add-two-numers' problem on leetcode
link: https://leetcode.com/problems/add-two-numbers/description/
"""
class Solution:
    """Solves the leetcode problem"""

    def enumerateList(self, l):
        """Enumerate elements of a linked list into a list"""
        returnArr = []
        curNode = l
        while curNode is not None:
            returnArr.append(curNode.val)
            curNode = curNode.next
        return returnArr


    def listToNum(self, l):
        """Converts a list into a number (e.g., [1, 2, 3] -> 123)"""
        total = 0
        for i, count in enumerate(l):
            tensPlaces = 10 ** i
            total += tensPlaces * count
        print(f'total: {total}')
        return total


    def numToReverseList(self, num):
        """Converts an integer into a reversed list (e.g., 123 -> [3, 2, 1])"""
        foo = str(num)
        returnList = [int(char) for char in foo]
        return returnList[::-1]


    def listToNodes(self, l):
        """Converts a list into a ListNode object"""
        listNode = ListNode()
        return listNode._array_to_list_node(l)


    def addTwoNumbers(self, l1, l2) -> list:
        """Adds two numbers represented by linked lists"""
        list1 = self.enumerateList(l1)
        list2 = self.enumerateList(l2)
        num1 = self.listToNum(list1)
        num2 = self.listToNum(list2)
        total = num1 + num2
        reversedList = self.numToReverseList(total)
        return self.listToNodes(reversedList)
