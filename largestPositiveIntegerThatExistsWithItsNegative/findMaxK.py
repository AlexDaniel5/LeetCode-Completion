class Solution(object):
    def findMaxK(self, nums):
        nums.sort()
        r = len(nums) - 1
        l = 0
        while l < r:
            # Left pointer or right pointer must stay in positive/negative
            if nums[l] > 0 or nums[r] < 0:
                return -1
            # Negative version is larger
            if abs(nums[l]) > nums[r]:
                l += 1
            # Negative version is smaller
            elif abs(nums[l]) < nums[r]:
                r -= 1
            # Numbers match
            else:
                return nums[r]
        return -1  
    
print(Solution().findMaxK([-1,10,6,7,-7,1])) # 7