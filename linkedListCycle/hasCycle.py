# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slowPointer = head
        fastPointer = head
        # While the end of the linked list isn't encountered
        while (fastPointer != None and fastPointer.next != None):
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            # Check if the pointers are on the same node
            if (slowPointer == fastPointer):
                return True
        return False # The end of the linked list is reached

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creating a cycle
print(Solution().hasCycle(node1)) # True