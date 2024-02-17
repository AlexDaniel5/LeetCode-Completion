class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        differenceList = []
        differenceList.append(0)
        for i in range(len(heights) - 1):
            difference = heights[i + 1] - heights[i]
            if difference > 0:
                bricks -= difference
                differenceList.append(difference)
            if bricks < 0:
                if ladders > 0:
                    ladders -= 1
                else: 
                    return i
        return len(heights) - 1