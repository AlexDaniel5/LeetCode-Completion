class Solution(object):
    def findDuplicate(self, nums):
        slow = 0
        fast = 0
        # Find a cycle in the list
        while True:
            slow = nums[slow] # Move one step forward
            fast = nums[nums[fast]] # Move two steps forward
            if slow == fast:
                break
        slow2 = 0
        # Discover duplicate number
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            
print(Solution().findDuplicate([1,3,4,2,2])) # 2