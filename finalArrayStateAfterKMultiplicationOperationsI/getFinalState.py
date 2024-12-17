import heapq

class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        n = len(nums)
        heap = []
        # Create a min-heap to store pairs of (value, index)
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
        while k > 0:
            element, index = heapq.heappop(heap)
            # Update the actual list
            nums[index] = element * multiplier
            # Push the updated value to the correct location in the list
            heapq.heappush(heap, (nums[index], index))
            k -= 1
        return nums
    
print(Solution().getFinalState([1,3,5], 5, 3)) # [27, 9, 15]