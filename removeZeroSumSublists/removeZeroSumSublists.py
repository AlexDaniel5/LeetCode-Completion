# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeZeroSumSublists(self, head):
        # Create the head as 0 and point its next to the original head
        front = ListNode(0, head)
        ptr = front
        prefixSum = 0
        seen = {0: front}
        # Calculate the prefix sum of all nodes and store them in the hash map
        while ptr:
            prefixSum += ptr.val
            seen[prefixSum] = ptr
            ptr = ptr.next
        
        ptr = front
        prefixSum = 0

        # Traverse through the list again skipping nodes with zero sums
        while ptr:
            prefixSum += ptr.val
             # If there exists a key with the same value in the hashmap skip all nodes in-between
            ptr.next = seen[prefixSum].next
            ptr = ptr.next
        return front.next

# Example
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(-3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(1)
result = Solution().removeZeroSumSublists(head) # 3 1
while result:
    print(result.val, end=" ")
    result = result.next