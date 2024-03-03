# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        # Find length of linked list
        current = head
        while current:
            length += 1
            current = current.next
        # Edge case: If we're deleting the head itself
        if length == n:
            return head.next
        # Update the pointers to skip the node to be deleted
        current = head
        for i in range(length - n - 1):
            current = current.next
        current.next = current.next.next
        return head
        