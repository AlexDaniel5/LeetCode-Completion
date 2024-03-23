# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        turtle = head
        rabbit = head
        # Find middle of linked list
        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            turtle = turtle.next
            
        prev = None
        # Reverse second half of linked list
        while turtle:
            tmp = turtle.next
            turtle.next = prev
            prev = turtle
            turtle = tmp

        left = head
        right = prev
        # Reorder list
        while right.next: # Must be next or a cycle error occurs
            lPtr = left.next
            rPtr = right.next
            left.next = right
            right.next = lPtr
            left = lPtr
            right = rPtr
        return head
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

head = Solution().reorderList(head) # 1, 4, 2, 3

while head:
    print(head.val, end=" ")
    head = head.next