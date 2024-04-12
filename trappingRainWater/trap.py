class Solution(object):
    def trap(self, height):
        length = len(height)
        maxRights = [0] * length
        maxRight = 0
        
        # Fill in the array of maximum heights on the right
        for i in reversed(range(length)):
            # Store the value after updating maxRight to capture the previous height; right height
            maxRights[i] = maxRight
            if maxRight < height[i]:
                maxRight = height[i]

        result = 0
        maxLeft = 0
        for i in range(length):
            # Determine the minimum height between the left and right heights, indicating potential water level
            minimum = min(maxRights[i], maxLeft)
            if minimum > height[i]:
                result += minimum - height[i]
            # Update maxLeft following a similar logic as the previous loop
            if maxLeft < height[i]:
                maxLeft = height[i]
        return result
    
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6