# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNodes(self, head):
        highest, highestIndex, nodes, i = 1, 1, 1, 1
        curr, nex = head, head.next
        while nex is not None:
            if nex.val <= curr.val:
                nodes += 1
            else:
                highest = max(highest, nodes)
                highestIndex = i - nodes
                nodes = 1
            nex = nex.next
            curr = curr.next
            i += 1
        if nodes > highest:
            highest = nodes
            highestIndex = i - nodes
        curr = head
        for _ in range(highestIndex):
            curr = curr.next
        newHead = curr
        # My thought process wasn't on track here
        curr.next = None
        return newHead
    
head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(13)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(8)

head = Solution().removeNodes(head) # 13 -> 8
while head is not None:
    print(head.val)
    head = head.next