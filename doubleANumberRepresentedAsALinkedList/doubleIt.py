# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def doubleIt(self, head):
        # Reverses Linked List
        def reverse(head):
            prev, cur = None, head
            while cur:
                tmp = cur.next
                cur.next = prev
                prev, cur = cur, tmp
            return prev
        head = reverse(head)
        cur = head
        prev = head
        carry = 0
        # Multiply each node by 2 and add the carry to the next node
        while cur:
            total = cur.val * 2 + carry
            cur.val = total % 10
            carry = total // 10
            prev = cur
            cur = cur.next
        # If there's a carry on the last digit add a new node to represent it
        if carry > 0:
            prev.next = ListNode(carry)
        return reverse(head)
    

head = ListNode(1)
head.next = ListNode(8)
head.next.next = ListNode(9)

head = Solution().doubleIt(head) # 3 -> 7 -> 8
while head is not None:
    print(head.val)
    head = head.next