# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution(object):
    def middleNode(self, head):
        length = 0
        node = head
        # Determine the length of linked list
        while node != None:
            length += 1
            node = node.next
        node = head
        # Iterate until the middle of the linked list is reached
        for i in range(length//2):
            node = node.next
        return node