# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        ptr = list1
        i = 1
        # Traverse list1 to find the insertion point for list2
        while i < a:
            ptr = ptr.next
            i += 1
        head = ptr
        i -= 2
        # Traverse list1 to find the end point for list2's insertion
        while i < b:
            ptr = ptr.next
            i += 1
        tail = ptr
        # Connect list2 at the insertion point determined by head
        head.next = list2
        # Find the end of the merged list and connect it to list1's tail
        while head.next:
            head = head.next
        head.next = tail
        return list1

head1 = ListNode(10)
head1.next = ListNode(1)
head1.next.next = ListNode(13)
head1.next.next.next = ListNode(6)
head1.next.next.next.next = ListNode(9)
head1.next.next.next.next.next = ListNode(5)

head2 = ListNode(1000000)
head2.next = ListNode(1000001)
head2.next.next = ListNode(1000002)

mergedList = Solution().mergeInBetween(head1, 3, 4, head2) # 10, 1, 13, 1000000, 1000001, 1000002, 5

while mergedList:
    print(mergedList.val, end=" ")
    mergedList = mergedList.next