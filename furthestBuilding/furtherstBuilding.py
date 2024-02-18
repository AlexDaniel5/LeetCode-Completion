import heapq

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        heap = []
        # Iterate until the second last building to calculate the difference in heights
        for i in range(len(heights) - 1):
            difference = heights[i + 1] - heights[i]
            # If ascending a building, use bricks to climb
            if difference > 0:
                bricks -= difference
                heapq.heappush(heap, -difference) # Push the difference to the heap
            # If out of bricks, utilize ladders
            if bricks < 0:
                if ladders > 0:
                    ladders -= 1
                    bricks += -heapq.heappop(heap) # Add the number of bricks gained for the tallest climb
                # If both bricks and ladders are exhausted, return
                else:
                    return i
        # If iterated through all the heights without return, return the last index
        return len(heights) - 1
    
solution = Solution()
buildings = [4,12,2,7,3,18,20,3,19]
print(solution.furthestBuilding(buildings)) # 7