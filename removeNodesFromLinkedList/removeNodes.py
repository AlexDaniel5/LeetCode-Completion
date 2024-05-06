# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNodes(self, head):
        # Reverses the linked list
        def reverse(head):
            prev, cur = None, head
            while cur:
                tmp = cur.next
                cur.next = prev
                prev, cur = cur, tmp
            return prev
        
        head = reverse(head)
        cur = head
        while cur.next:
            # Remove the next node if it's smaller than the current node's value
            if cur.next.val < cur.val:
                cur.next = cur.next.next
            # Else keep the node
            else:
                cur = cur.next
        return reverse(head)
    
head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(13)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(8)

head = Solution().removeNodes(head) # 13 -> 8
while head is not None:
    print(head.val)
    head = head.next