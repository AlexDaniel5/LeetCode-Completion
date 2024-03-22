class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
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
        # Check palindrome
        while right:
            if left.val != right.val:
                return False
            right = right.next
            left = left.next
        return True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print(Solution().isPalindrome(head)) # True