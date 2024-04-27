class Solution(object):
    def maxArea(self, height):
        r = len(height) - 1
        l = 0
        leftHeight = height[0]
        rightHeight = height[r]
        maxArea = (r - l) * min(leftHeight, rightHeight)
        while r != l:
            # Move left window
            if leftHeight < rightHeight:
                l += 1
                leftHeight = height[l]
            # Move right window
            else:
                r -= 1
                rightHeight = height[r]
            # Update maxArea, if new area is greater
            maxArea = max(maxArea, (r - l) * min(leftHeight, rightHeight))
        return maxArea  
    
print(Solution().maxArea([1,8,6,2,5,4,8,3,7])) # 49