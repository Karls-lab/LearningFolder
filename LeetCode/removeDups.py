# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Input: head = [1,1,2]
# Output: [1,2]
class Solution:
    def deleteDuplicates(self, head: ListNode):
        node = head
        while node != None:
            if node.next  == node.val and node.next.next != None:
                node.next = node.next.next
            node = node.next
        return head

sol = Solution()

node3 = ListNode(2, next=None)
node2 = ListNode(1, next=node3)
node1 = ListNode(1, next = node2)
head = node1
sol.deleteDuplicates(head)
print(head.next.next.val)