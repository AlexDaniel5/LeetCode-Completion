class Solution(object):
    def findMinArrowShots(self, points):
        points.sort()
        length = len(points)
        ans = length # Set the answer to worst case scenario
        prev = points[0]
        # For every list check if their intervals overlap
        for i in range(1, length):
            curr = points[i]
            # If the interval overlaps with the previous interval
            if curr[0] <= prev[1]:
                # Take one away from the answer
                ans -= 1
                # Determine which interval has a shorter max distance for the next comparison
                prev = [curr[0], min(curr[1], prev[1])]
            # The interval didn't overlap
            else:
                prev = curr
        return ans   

print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])) # 2 