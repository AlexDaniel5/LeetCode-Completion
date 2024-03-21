# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        ptr = head
        prev = None
        nex = None

        while ptr != None:
            # Remember the next node
            nex = ptr.next
            # Set the next node to the previous node
            ptr.next = prev
            prev = ptr
            # Move to the next node
            ptr = nex
        # Set the head to the last node of the original linked list
        head = prev
        return head
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
result = Solution().reverseList(head) # 5, 4, 3, 2, 1
while result != None:
    print(result.val, end=" ")
    result = result.next
        