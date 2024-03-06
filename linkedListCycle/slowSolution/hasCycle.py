# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        node = head
        nodes = []
        # While we haven't reached the end of the linked list
        while node != None:
            # If we already encountered the number return True
            if node in nodes:
                return True
            nodes.append(node)
            node = node.next
        return False # No cycle
    
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creating a cycle
print(Solution().hasCycle(node1)) # True