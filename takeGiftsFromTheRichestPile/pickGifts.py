import math
import heapq

class Solution(object):
    def pickGifts(self, gifts, k):
        # Convert list into negative counterpart
        maxHeap = [-x for x in gifts]
        # Convert list into heap
        heapq.heapify(maxHeap)
        for _ in range(k):
            largest = -heapq.heappop(maxHeap)
            updatedValue = int(math.sqrt(largest))
            # Insert the updated value into the heap, maintaining the max-heap property
            heapq.heappush(maxHeap, -updatedValue)
        # Undo negation
        return sum([-x for x in maxHeap])
    
print(Solution().pickGifts([25,64,9,4,100], 4)) # 29